import os

def generate_yearly_md_files():
    # 获取当前目录（假设脚本运行在 /blog 下）
    current_dir = os.getcwd()
    blog_dir = current_dir  # 因为脚本运行在 /blog 下

    # 遍历 /blog 下的所有子文件夹
    for dir_name in os.listdir(blog_dir):
        # 检查是否是年份文件夹（假设年份是 4 位数字）
        if os.path.isdir(os.path.join(blog_dir, dir_name)) and dir_name.isdigit():
            year = dir_name
            year_dir = os.path.join(blog_dir, year)
            output_file = f"{year}.md"
            
            # 收集该年份的所有文章标题和链接
            articles = []
            for file_name in os.listdir(year_dir):
                if file_name.endswith(".md"):  # 只处理 Markdown 文件
                    file_path = os.path.join(year_dir, file_name)
                    # 打开文件并读取标题
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            first_line = f.readline().strip()
                            if first_line.startswith("# "):
                                title = first_line[2:]  # 去掉开头的 #
                                articles.append({
                                    "title": title,
                                    "link": f"/blog/{year}/{file_name}"
                                })
                            else:
                                print(f"Warning: {file_name} 的第一行不是有效的 h1 标题。")
                    except Exception as e:
                        print(f"Error reading {file_name}: {e}")

            # 生成年份的 Markdown 文件
            if articles:
                with open(output_file, "w", encoding="utf-8") as out_f:
                    out_f.write(f"# {year}\n\n")
                    out_f.write("以下是一些相关的文章推荐：\n")
                    for article in articles:
                        out_f.write(f"- [{article['title']}]({article['link']})\n\n")
                print(f"成功生成 {output_file} 文件，包含 {len(articles)} 篇文章。")
            else:
                print(f"未找到 {year} 文件夹中的文章，因此未生成文件 {output_file}。")

if __name__ == "__main__":
    generate_yearly_md_files()