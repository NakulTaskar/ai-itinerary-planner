"""Export helpers."""

from .models import Itinerary


def to_markdown(it: Itinerary) -> str:
    lines = [f"# {it.trip_title}", "", it.overview, ""]
    for d in it.days:
        lines += [f"## Day {d.day} · {d.date} — {d.theme}", ""]
        for a in d.activities:
            lines.append(
                f"- **{a.time_of_day}: {a.title}** ({a.place}) — {a.description} "
                f"_[{a.estimated_cost}]_"
            )
        lines += ["", f"🍽️ **Food:** {d.food_recommendation}",
                  f"💰 **Day cost:** {d.daily_cost}", ""]
    lines += [f"## 💰 Estimated total budget\n\n{it.estimated_total_budget}", ""]
    lines += ["## 🎒 Packing list", ""] + [f"- {p}" for p in it.packing_list] + [""]
    lines += ["## 💡 Local tips", ""] + [f"- {t}" for t in it.local_tips] + [""]
    return "\n".join(lines)
