## Blog Reading Streak App

This web app tracks my daily blog-reading stats and generates dynamic streaks.

### Features
- Track daily blog-reading progress.
- Generate GitHub-compatible streak stats.
- API endpoint to retrieve streak information.

### Live Demo of Streak Stats:

@app.route('/readme', methods=['GET'])
def generate_readme():
    streak = get_streak().get_json()
    markdown = f"""

    ### Blog Reading Streak

    - **Current Streak:** {streak['current_streak']} days
    - **Max Streak:** {streak['max_streak']} days
    - **Blogs Read This Week:** {sum(reading_log.values())}

    ![Blog Streak](https://img.shields.io/badge/Blog_Streak-{streak['current_streak']}_days-green)
    """
    return markdown

