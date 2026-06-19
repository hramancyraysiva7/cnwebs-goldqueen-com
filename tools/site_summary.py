import json
import sys

SITE_DATA = [
    {
        "name": "GoldQueen",
        "url": "https://cnwebs-goldqueen.com",
        "keywords": ["赏金女王", "gold queen", "slot", "online casino"],
        "tags": ["娱乐", "博彩", "老虎机"],
        "description": "赏金女王主题在线娱乐平台，提供老虎机、百家乐等热门游戏。"
    },
    {
        "name": "Demo Site",
        "url": "https://example.com",
        "keywords": ["demo", "sample", "test"],
        "tags": ["示例", "测试"],
        "description": "仅用于演示的站点条目。"
    }
]

def build_summary(site):
    kw_str = ", ".join(site["keywords"])
    tag_str = ", ".join(site["tags"])
    summary_lines = [
        f"站点名称：{site['name']}",
        f"访问地址：{site['url']}",
        f"核心关键词：{kw_str}",
        f"标签：{tag_str}",
        f"简介：{site['description']}"
    ]
    return "\n".join(summary_lines)

def generate_full_report(sites):
    report_parts = []
    report_parts.append("========== 站点摘要报告 ==========")
    report_parts.append(f"共计 {len(sites)} 个站点\n")
    for idx, site in enumerate(sites, start=1):
        report_parts.append(f"--- 站点 {idx} ---")
        report_parts.append(build_summary(site))
        report_parts.append("")
    report_parts.append("========== 报告结束 ==========")
    return "\n".join(report_parts)

def export_to_json(sites, filepath="site_summary.json"):
    output = []
    for site in sites:
        output.append({
            "name": site["name"],
            "url": site["url"],
            "keywords": site["keywords"],
            "tags": site["tags"],
            "description": site["description"]
        })
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"JSON 文件已导出至：{filepath}")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--export-json":
        export_to_json(SITE_DATA)
        return
    report = generate_full_report(SITE_DATA)
    print(report)
    if len(sys.argv) > 1 and sys.argv[1] == "--save":
        with open("site_report.txt", "w", encoding="utf-8") as f:
            f.write(report)
        print("报告已保存至 site_report.txt")

if __name__ == "__main__":
    main()