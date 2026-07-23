import random

def get_choices():
    """Get player choice from user input."""
    player_input = input("\n请输入你的选择 (r/p/s 或 q 退出): ").lower()
    
    # 检查是否退出
    if player_input == "q":
        return None, None
    
    # 将快捷方式转换为完整选项
    choice_map = {
        "r": "rock",
        "p": "paper",
        "s": "scissors",
        "rock": "rock",
        "paper": "paper",
        "scissors": "scissors"
    }
    
    if player_input not in choice_map:
        print("❌ 无效选项！请选择 r(rock)、p(paper)、s(scissors) 或 q(退出)。")
        return get_choices()
    
    player_choice = choice_map[player_input]
    computer_choice = random.choice(["rock", "paper", "scissors"])
    return player_choice, computer_choice


def check_winner(player, computer):
    """Check the winner of the round."""
    if player == computer:
        return "平局"
    
    # 定义获胜规则
    winning_combinations = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    
    if winning_combinations[player] == computer:
        return "赢"
    else:
        return "输"


def display_round_result(player, computer, result):
    """Display the result of the round."""
    print(f"\n你的选择: {player}")
    print(f"计算机的选择: {computer}")
    print(f"结果: {result}")


def play_game():
    """Main game loop."""
    player_score = 0
    computer_score = 0
    
    print("=" * 40)
    print("欢迎来到石头剪刀布游戏！")
    print("=" * 40)
    print("\n快捷方式: r(rock) p(paper) s(scissors) q(退出)")
    
    while True:
        # 获取玩家和计算机的选择
        player_choice, computer_choice = get_choices()
        
        # 检查是否退出游戏
        if player_choice is None:
            break
        
        # 判断赢家
        result = check_winner(player_choice, computer_choice)
        
        # 显示结果
        display_round_result(player_choice, computer_choice, result)
        
        # 更新分数
        if result == "赢":
            player_score += 1
            print("🎉 恭喜，你赢了！")
        elif result == "输":
            computer_score += 1
            print("😞 很遗憾，你输了！")
        else:
            print("🤝 平局！")
        
        # 显示当前分数
        print(f"\n当前分数 - 你: {player_score}, 计算机: {computer_score}")
    
    # 显示最终分数
    print("\n" + "=" * 40)
    print("游戏结束！")
    print("=" * 40)
    print(f"最终分数:")
    print(f"你: {player_score}")
    print(f"计算机: {computer_score}")
    
    if player_score > computer_score:
        print("\n🏆 恭喜！你赢得了整个游戏！")
    elif player_score < computer_score:
        print("\n💻 计算机赢得了游戏。下次加油！")
    else:
        print("\n🤝 你和计算机打成平手！")
    
    print("=" * 40)


if __name__ == "__main__":
    play_game()