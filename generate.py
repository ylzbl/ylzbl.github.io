import os

def generate_summary(root_dir):
    # 定义博客目录路径
    blog_dir = os.path.join(root_dir, 'blog')
    
    # 检查是否存在 blog 子目录
    if not os.path.exists(blog_dir):
        print(f"未找到 {blog_dir} 子目录")
        return
    
    # 初始化 SUMMARY.md 内容
    summary_lines = ["* [Home](README.md)\n"]
    
    # 遍历 blog 子目录
    for subdir in os.listdir(blog_dir):
        subdir_path = os.path.join(blog_dir, subdir)
        
        # 确保是文件夹
        if os.path.isdir(subdir_path):
            # 添加 section 标题
            summary_lines.append(f"* {subdir}\n")
            
            # 遍历子文件夹中的 .md 文件
            for md_file in os.listdir(subdir_path):
                if md_file.endswith('.md') and md_file != 'SUMMARY.md':
                    # 生成相对路径
                    file_path = os.path.join(subdir, md_file)
                    # 添加到 SUMMARY.md
                    summary_lines.append(f"    * [{md_file[:-3]}]({file_path})\n")
    
    # 定义 SUMMARY.md 文件路径
    summary_path = os.path.join(root_dir, 'SUMMARY.md')
    
    # 检查是否已存在 SUMMARY.md
    if os.path.exists(summary_path):
        print(f"{summary_path} 已存在，不会覆盖")
        return
    
    # 写入 SUMMARY.md
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.writelines(summary_lines)
    
    print(f"{summary_path} 已生成")

# 调用脚本，传入当前脚本所在目录的根目录
if __name__ == "__main__":
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    generate_summary(current_dir)