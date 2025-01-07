import json

def generate_roadmap(goals):
    roadmap = "### 🚀 **Project Roadmap**\n\n"
    
    for index, goal in enumerate(goals, start=1):
        match goal["status"]:
            case "completed":
                status_emoji = "✅"
            case "missed":
                status_emoji = "❌"
            case "inProgress":
                status_emoji = "⏳"
            case "planned":
                status_emoji = "⏰"
            case _:
                status_emoji = "❓"
        
        roadmap += f"{index}️⃣ **Goal {index}:** {goal['title']} {goal['emoji']} {status_emoji}\n"
        roadmap += f"   📅 Deadline: {goal['deadline']}\n"
        roadmap += f"   🎯 Subtasks:\n"
        
        for subtask in goal['subtasks']:
            match subtask["status"]:
                case "completed":
                    status_emoji = "✅"
                case "missed":
                    status_emoji = "❌"
                case "inProgress":
                    status_emoji = "⏳"
                case "planned":
                    status_emoji = "⏰"
                case _:
                    status_emoji = "❓"
            roadmap += f"   - {subtask['emoji']} {subtask['task']} {status_emoji}\n"
        
        roadmap += "\n"
    
    return roadmap

if __name__ == '__main__':
    # Load goals from roadmap.json
    with open("roadmap.json", "r") as f:
        goals = json.load(f)

    # Generate and save the Markdown
    markdown_content = generate_roadmap(goals)
    with open("roadmap.md", "w") as f:
        f.write(markdown_content)

    print("Roadmap saved to 'roadmap.md'!")