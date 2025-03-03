import os

def generate_yearly_md_files():
    current_dir = os.getcwd()  # 获取当前目录（假设脚本运行在 /blog 下）
    blog_dir = current_dir
    output_files = []  # 用于记录已处理的年份，避免重复生成

    # 遍历 /blog 下的所有子文件夹和文件
    for dir_name in os.listdir(blog_dir):
        dir_path = os.path.join(blog_dir, dir_name)
        if os.path.isdir(dir_path) and dir_name.isdigit():  # 确保是年份文件夹
            year = dir_name
            year_dir = dir_path
            output_file = f"{year}.md"

            # 检查是否已处理过该年份，避免重复生成
            if year in output_files:
                continue
            output_files.append(year)

            # 收集该年份的所有文章标题、链接和发布日期
            articles = []
            for file_name in os.listdir(year_dir):
                if file_name.endswith(".md"):  # 只处理 Markdown 文件
                    file_path = os.path.join(year_dir, file_name)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            first_line = f.readline().strip()
                            # 提取标题，假设标题是文件的首行，并且以# 开头
                            if first_line.startswith("# "):
                                title = first_line[2:]  # 去掉开头的 #
                                # 提取发布日期，假设文件名包含日期格式（例如 20140528）
                                # 文件名格式应为 YYYYMMDD_*.md
                                # 从文件名中提取日期
                                date_part = file_name.split("_")[0]
                                if len(date_part) == 8 and date_part.isdigit():
                                    # 将日期格式从 YYYYMMDD 转换为 YYYY-MM-DD
                                    year_part = date_part[:4]
                                    month_part = date_part[4:6]
                                    day_part = date_part[6:8]
                                    publish_date = f"{year_part}-{month_part}-{day_part}"
                                else:
                                    publish_date = "日期未知"

                                article_info = {
                                    "title": title,
                                    "link": f"/blog/{year}/{file_name}",
                                    "date": publish_date
                                }
                                articles.append(article_info)
                            else:
                                print(f"Warning: {file_name} 的第一行不是有效的 h1 标题。")
                    except Exception as e:
                        print(f"Error reading {file_name}: {e}")

            # 生成年份的 Markdown 文件
            if articles:
                with open(output_file, "w", encoding="utf-8") as out_f:
                    out_f.write(f"# {year} 年文章索引\n\n")
                    for article in articles:
                        out_f.write(f"- [{article['title']}]({article['link']}) {article['date']}\n\n")
                print(f"成功生成 {output_file} 文件，包含 {len(articles)} 篇文章。")
            else:
                print(f"未找到 {year} 文件夹中的文章，因此未生成文件 {output_file}。")

if __name__ == "__main__":
    generate_yearly_md_files()