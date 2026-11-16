#!/usr/bin/env python3
"""Check sequential shot-plan timing. Standard library only; never edits inputs."""

import argparse
import json
import math
import sys
from pathlib import Path


def number(value, positive=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    try:
        return math.isfinite(value) and (value > 0 if positive else value >= 0)
    except OverflowError:
        return False


def check(plan):
    errors, warnings, timeline = [], [], []
    if not isinstance(plan, dict):
        return {"ok": False, "errors": ["顶层必须为JSON对象。"], "warnings": []}
    shots = plan.get("shots")
    if not isinstance(shots, list) or not shots:
        return {"ok": False, "errors": ["shots必须是非空数组。"], "warnings": []}

    fps = plan.get("fps")
    if fps is not None and not number(fps, positive=True):
        errors.append("fps必须为正的有限数值。")
        fps = None
    tolerance = plan.get("tolerance_s", 1 / fps if fps else 0.001)
    if not number(tolerance):
        errors.append("tolerance_s必须为非负有限数值。")
        tolerance = 0.001

    target = plan.get("target_duration_s")
    limits = None
    if number(target, positive=True):
        limits = (target, target)
    elif (isinstance(target, list) and len(target) == 2
          and all(number(v, positive=True) for v in target)
          and target[0] <= target[1]):
        limits = tuple(target)
    else:
        errors.append("target_duration_s须为正数，或递增的[最短, 最长]秒数。")

    durations, overlaps, ids = [], [], []
    seen, unknown_sources = set(), []
    for index, shot in enumerate(shots):
        label = f"第{index + 1}镜"
        if not isinstance(shot, dict):
            errors.append(f"{label}必须为对象。")
            durations.append(0)
            overlaps.append(0)
            ids.append(label)
            continue
        shot_id = shot.get("shot_id")
        if not isinstance(shot_id, str) or not shot_id.strip():
            errors.append(f"{label}缺少非空shot_id。")
            shot_id = label
        else:
            shot_id = shot_id.strip()
            if shot_id in seen:
                errors.append(f"镜号重复：{shot_id}。")
            seen.add(shot_id)
        ids.append(shot_id)

        duration = shot.get("duration_s")
        if not number(duration, positive=True):
            errors.append(f"{shot_id}: duration_s必须为正的有限秒数。")
            duration = 0
        durations.append(duration)
        overlap = shot.get("transition_out_s", 0)
        if not number(overlap):
            errors.append(f"{shot_id}: transition_out_s必须为非负有限秒数。")
            overlap = 0
        overlaps.append(overlap)

        handles = []
        for key in ("handle_in_s", "handle_out_s"):
            value = shot.get(key, 0)
            if not number(value):
                errors.append(f"{shot_id}: {key}必须为非负有限秒数。")
                value = 0
            handles.append(value)
        source = shot.get("usable_source_s")
        if source is None:
            unknown_sources.append(shot_id)
        elif not number(source, positive=True):
            errors.append(f"{shot_id}: usable_source_s必须为正数或null。")
        elif source + tolerance < duration + sum(handles):
            errors.append(
                f"{shot_id}: 需{duration + sum(handles):g}秒（含余量），"
                f"解释后的可用素材仅{source:g}秒。"
            )
        for key in ("purpose", "camera", "audio"):
            if not isinstance(shot.get(key), str) or not shot[key].strip():
                warnings.append(f"{shot_id}: 建议补充{key}文字说明。")

    for index, overlap in enumerate(overlaps):
        if index == len(shots) - 1:
            if overlap != 0:
                errors.append(f"{ids[index]}: 最后一镜的transition_out_s必须为0。")
        elif overlap > min(durations[index], durations[index + 1]) + 1e-9:
            errors.append(f"{ids[index]}: 转场重叠超过相邻片段长度。")
        incoming = overlaps[index - 1] if index else 0
        if incoming + overlap > durations[index] + 1e-9:
            errors.append(f"{ids[index]}: 进出转场相交；本工具不支持三镜重叠。")

    overlap_total = sum(overlaps[:-1])
    total = sum(durations) - overlap_total
    if not number(total, positive=True):
        errors.append("计算出的成片时长必须为正的有限数值。")
    elif limits and not limits[0] - tolerance <= total <= limits[1] + tolerance:
        errors.append(f"总长{total:g}秒，不在目标{limits[0]:g}–{limits[1]:g}秒内。")

    cursor = 0
    for index, duration in enumerate(durations):
        timeline.append({"shot_id": ids[index], "start_s": round(cursor, 6),
                         "end_s": round(cursor + duration, 6)})
        cursor += duration - (overlaps[index] if index < len(shots) - 1 else 0)
    if unknown_sources:
        warnings.append("未核实可用素材长度：" + "、".join(unknown_sources)
                        + "。这是计划核算，不能视为素材已经拍摄或生成。")
    # Very large finite inputs may overflow their sums; keep JSON standards compliant.
    safe = lambda value: round(value, 6) if math.isfinite(value) else None
    for row in timeline:
        row["start_s"], row["end_s"] = safe(row["start_s"]), safe(row["end_s"])
    return {"ok": not errors, "shot_count": len(shots),
            "clip_sum_s": safe(sum(durations)), "overlap_s": safe(overlap_total),
            "program_duration_s": safe(total), "errors": errors,
            "warnings": warnings, "timeline": timeline}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path, help="JSON shot plan")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    try:
        result = check(json.loads(args.plan.read_text(encoding="utf-8-sig")))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        result = {"ok": False, "errors": [f"无法读取有效JSON：{exc}"], "warnings": []}
        code = 2
    else:
        code = 0 if result["ok"] else 1
    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    else:
        print("核算通过" if result["ok"] else "需要修正")
        if "program_duration_s" in result:
            print(f"镜头数：{result['shot_count']}；成片时长：{result['program_duration_s']}秒")
        for issue in result["errors"]:
            print("错误：" + issue)
        for issue in result["warnings"]:
            print("提醒：" + issue)
    return code


if __name__ == "__main__":
    sys.exit(main())
