import random
from trivia_dictionary import trivia_categories, category_colors
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font("Chicle-Regular.ttf", 48)
question_font = pygame.font.Font("Chicle-Regular.ttf", 32)
answer_font = pygame.font.Font("Chicle-Regular.ttf", 24)
clock = pygame.time.Clock()
running = True

# Constants for scoring and colors for buttons and text
SHORT_GAME = 10
MEDIUM_GAME = 25
LONG_GAME = 50
BUTTON_COLOR = "#1a1a2e"
TEXT_COLOR = "#ffd700"

# Track asked_questions to prevent repeats during same game
asked_questions = set()
player_score = 0
target_score = 0
correct_answers = 0
incorrect_answers = 0
current_question = None
current_category = None

# Game states
game_state = "welcome"
player_name = ""
game_length = ""
game_difficulty = ""
player_difficulty = ""
category_choice = ""
feedback_text = ""

button_color = "#1a1a2e"
text_color = "#c0c0c0"

short_game_rect = pygame.Rect(275, 125, 350, 60)
medium_game_rect = pygame.Rect(275, 225, 350, 60)
long_game_rect = pygame.Rect(275, 325, 350, 60)

easy_game_difficulty_rect = pygame.Rect(275, 125, 250, 60)
medium_game_difficulty_rect = pygame.Rect(275, 225, 250, 60)
hard_game_difficulty_rect = pygame.Rect(275, 325, 250, 60)

fixed_difficulty_rect = pygame.Rect(275, 125, 250, 60)
mixed_difficulty_rect = pygame.Rect(275, 225, 250, 60)

category_rects = []
answer_rects = []

play_again_rect = pygame.Rect(275, 425, 250, 60)
exit_rect = pygame.Rect(275, 510, 250, 60)


def get_question_by_category(asked_questions, game_difficulty, category=None):
    """Pick a random or specific category and return one question, or None."""
    difficulty = {"E": "easy", "M": "medium", "H": "hard"}[game_difficulty]
    categories = list(trivia_categories.keys())
    if not categories:
        print("No categories available.")
        return None
    if category is None or category == "R":
        category = random.choice(categories)
    questions = trivia_categories.get(category, {}).get(difficulty, [])
    if not questions:
        print("No questions available for that category/difficulty.")
        return None
    # Filter out already asked questions
    available_questions = [q for q in questions if q["question"] not in asked_questions]
    if not available_questions:
        print("All questions in this category have been asked! Please choose another.")
        return None
    question = random.choice(available_questions)
    asked_questions.add(question["question"])
    return category, question


def wrap_text(text, font, max_width):
    current_line = ""
    completed_lines = []
    split_question = text.split(" ")
    for word in split_question:
        if font.size(current_line + " " + word)[0] > max_width:
            completed_lines.append(current_line)
            current_line = word
        else:
            current_line += " " + word
    completed_lines.append(current_line)
    return completed_lines
   

while running:
    screen.fill("#1a3a8f")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_state == "welcome":
                if event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(player_name) >= 1:
                        game_state = "game_length"
                else:
                    player_name += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if game_state == "game_length":
                        if short_game_rect.collidepoint(event.pos):
                            game_length = "S"
                            target_score = SHORT_GAME
                            game_state = "player_difficulty"
                        elif medium_game_rect.collidepoint(event.pos):
                            game_length = "M"
                            target_score = MEDIUM_GAME
                            game_state = "player_difficulty"
                        elif long_game_rect.collidepoint(event.pos):
                            game_length = "L"
                            target_score = LONG_GAME
                            game_state = "player_difficulty"

                elif game_state == "player_difficulty":
                    if fixed_difficulty_rect.collidepoint(event.pos):
                        player_difficulty = "F"
                        game_state = "fixed_difficulty"
                    elif mixed_difficulty_rect.collidepoint(event.pos):
                        player_difficulty = "M"
                        game_state = "mixed_difficulty"

                elif game_state == "fixed_difficulty":
                    if easy_game_difficulty_rect.collidepoint(event.pos):
                        game_difficulty = "E"
                        game_state = "category_mode"
                        category_choice = ""
                    elif medium_game_difficulty_rect.collidepoint(event.pos):
                        game_difficulty = "M"
                        game_state = "category_mode"
                        category_choice = ""
                    elif hard_game_difficulty_rect.collidepoint(event.pos):
                        game_difficulty = "H"
                        game_state = "category_mode"
                        category_choice = ""

                elif game_state == "mixed_difficulty":
                    if easy_game_difficulty_rect.collidepoint(event.pos):
                        game_difficulty = "E"
                        game_state = "category_mode"
                        category_choice = ""
                    elif medium_game_difficulty_rect.collidepoint(event.pos):
                        game_difficulty = "M"
                        game_state = "category_mode"
                        category_choice = ""
                    elif hard_game_difficulty_rect.collidepoint(event.pos):
                        game_difficulty = "H"
                        game_state = "category_mode"
                        category_choice = ""

                elif game_state == "category_mode":
                    for rect, category in category_rects:
                        if rect.collidepoint(event.pos):
                            category_choice = category
                            current_category, current_question = get_question_by_category(asked_questions, game_difficulty, category_choice)
                            game_state = "question"

                elif game_state == "question":
                    for rect, index in answer_rects:
                        if rect.collidepoint(event.pos):
                            if current_question["choices"][index] == current_question["correct_answer"]:
                                player_score += current_question["points"]
                                correct_answers += 1
                                feedback_text = f"Right! That's worth {current_question['points']} points!"
                                game_state = "feedback"
                            else:
                                incorrect_answers += 1
                                feedback_text = f"Wrong! The correct answer is {current_question['correct_answer']}."
                                game_state = "feedback"

                elif game_state == "feedback":
                    if player_score >= target_score:
                        game_state = "win"
                    else:
                        if player_difficulty == "M":
                                game_state = "mixed_difficulty"
                        else:
                            game_state = "category_mode"
                        category_choice = ""
                    feedback_text = ""

                elif game_state == "win":
                    if play_again_rect.collidepoint(event.pos):
                        player_score = 0
                        correct_answers = 0
                        incorrect_answers = 0
                        asked_questions = set()
                        current_question = None
                        player_name = ""
                        game_length = ""
                        game_difficulty = ""
                        player_difficulty = ""
                        category_choice = ""
                        feedback_text = ""
                        game_state = "welcome"     
                    elif exit_rect.collidepoint(event.pos):
                        running = False

    if game_state == "welcome":  
        # Welcome screen      
        welcome_surface = font.render("Welcome to Trivia Quest!", True, TEXT_COLOR)
        welcome_rect = welcome_surface.get_rect(center=(400, 50))
        screen.blit(welcome_surface, welcome_rect)
        # Player name button
        player_surface = font.render("Enter your name: ", True, TEXT_COLOR)
        player_rect = player_surface.get_rect(center=(400, 150))
        screen.blit(player_surface, player_rect)
        name_surface = font.render(player_name, True, TEXT_COLOR)
        name_rect = name_surface.get_rect(center=(400, 200))
        screen.blit(name_surface, name_rect)
    
    # Game length buttons
    if game_state == "game_length":
        game_length_surface = font.render("How long would you like to play?", True, TEXT_COLOR)
        game_length_surface_rect = game_length_surface.get_rect(center=(400, 50))
        screen.blit(game_length_surface, game_length_surface_rect)

        # Short game
        pygame.draw.rect(screen, BUTTON_COLOR, short_game_rect, border_radius=10)
        short_game_surface = font.render("Short - 10 points", True, TEXT_COLOR)
        short_game_surface_rect = short_game_surface.get_rect(center=short_game_rect.center)
        screen.blit(short_game_surface, short_game_surface_rect)
        
        # Medium game
        pygame.draw.rect(screen, BUTTON_COLOR, medium_game_rect, border_radius=10)
        medium_game_surface = font.render("Medium - 25 points", True, TEXT_COLOR)
        medium_game_surface_rect = medium_game_surface.get_rect(center=medium_game_rect.center)
        screen.blit(medium_game_surface, medium_game_surface_rect)

        # Long game
        pygame.draw.rect(screen, BUTTON_COLOR, long_game_rect, border_radius=10)
        long_game_surface = font.render("Long - 50 points", True, TEXT_COLOR)
        long_game_surface_rect = long_game_surface.get_rect(center=long_game_rect.center)
        screen.blit(long_game_surface, long_game_surface_rect)

    if game_state == "player_difficulty":
        player_difficulty_surface = font.render("Game Difficulty", True, TEXT_COLOR)
        player_difficulty_surface_rect = player_difficulty_surface.get_rect(center=(400, 50))
        screen.blit(player_difficulty_surface, player_difficulty_surface_rect)

        pygame.draw.rect(screen, BUTTON_COLOR, fixed_difficulty_rect, border_radius=10)
        fixed_difficulty_text_surface = font.render("Fixed", True, TEXT_COLOR)
        fixed_difficulty_text_rect = fixed_difficulty_text_surface.get_rect(center=fixed_difficulty_rect.center)
        screen.blit(fixed_difficulty_text_surface, fixed_difficulty_text_rect)

        pygame.draw.rect(screen, BUTTON_COLOR, mixed_difficulty_rect, border_radius=10)
        mixed_difficulty_text_surface = font.render("Mixed", True, TEXT_COLOR)
        mixed_difficulty_text_rect = mixed_difficulty_text_surface.get_rect(center=mixed_difficulty_rect.center)
        screen.blit(mixed_difficulty_text_surface, mixed_difficulty_text_rect)

    if game_state == "fixed_difficulty":
        # Fixed difficulty
        fixed_difficulty_surface = font.render("Choose Difficulty", True, TEXT_COLOR)
        fixed_difficulty_surface_rect = fixed_difficulty_surface.get_rect(center=(400, 50))
        screen.blit(fixed_difficulty_surface, fixed_difficulty_surface_rect)

        pygame.draw.rect(screen, BUTTON_COLOR, easy_game_difficulty_rect, border_radius=10)
        easy_game_surface = font.render("Easy", True, TEXT_COLOR)
        easy_game_surface_rect = easy_game_surface.get_rect(center=easy_game_difficulty_rect.center)
        screen.blit(easy_game_surface, easy_game_surface_rect)

        pygame.draw.rect(screen, BUTTON_COLOR, medium_game_difficulty_rect, border_radius=10)
        medium_game_surface = font.render("Medium", True, TEXT_COLOR)
        medium_game_surface_rect = medium_game_surface.get_rect(center=medium_game_difficulty_rect.center)
        screen.blit(medium_game_surface, medium_game_surface_rect)

        pygame.draw.rect(screen, BUTTON_COLOR, hard_game_difficulty_rect, border_radius=10)
        hard_game_surface = font.render("Hard", True, TEXT_COLOR)
        hard_game_surface_rect = hard_game_surface.get_rect(center=hard_game_difficulty_rect.center)
        screen.blit(hard_game_surface, hard_game_surface_rect)

    if game_state == "mixed_difficulty":
        # Mixed difficulty
        mixed_difficulty_surface = font.render("Choose Difficulty", True, TEXT_COLOR)
        mixed_difficulty_surface_rect = mixed_difficulty_surface.get_rect(center=(400, 50))
        screen.blit(mixed_difficulty_surface, mixed_difficulty_surface_rect)

        pygame.draw.rect(screen, BUTTON_COLOR, easy_game_difficulty_rect, border_radius=10)
        easy_game_surface = font.render("Easy", True, TEXT_COLOR)
        easy_game_surface_rect = easy_game_surface.get_rect(center=easy_game_difficulty_rect.center)
        screen.blit(easy_game_surface, easy_game_surface_rect)

        pygame.draw.rect(screen, BUTTON_COLOR, medium_game_difficulty_rect, border_radius=10)
        medium_game_surface = font.render("Medium", True, TEXT_COLOR)
        medium_game_surface_rect = medium_game_surface.get_rect(center=medium_game_difficulty_rect.center)
        screen.blit(medium_game_surface, medium_game_surface_rect)

        pygame.draw.rect(screen, BUTTON_COLOR, hard_game_difficulty_rect, border_radius=10)
        hard_game_surface = font.render("Hard", True, TEXT_COLOR)
        hard_game_surface_rect = hard_game_surface.get_rect(center=hard_game_difficulty_rect.center)
        screen.blit(hard_game_surface, hard_game_surface_rect)

    if game_state == "category_mode":
        category_rects = []
        category_mode_surface = font.render("Categories", True, TEXT_COLOR)
        category_mode_surface_rect = category_mode_surface.get_rect(center=(400, 50))
        screen.blit(category_mode_surface, category_mode_surface_rect)
        
        for i, category in enumerate(trivia_categories):
            # Draw.rect expects in order: surface,color,tuple for rectangle(?, ?, ?, ?)
            """ Grid is 718px wide on an 800px screen. To center it, left offset would be (800 - 718) // 2 = 41px."""
            column = i % 3
            row = i // 3
            x = column * 226 + column * 20 + 41
            y = row * 75 + 100 + row * 10
            rect = pygame.Rect(x, y, 226, 75)

            difficulty = {"E": "easy", "M": "medium", "H": "hard"}[game_difficulty]
            questions = trivia_categories.get(category, {}).get(difficulty, [])
            available_questions = [q for q in questions if q["question"] not in asked_questions]

            if available_questions:
                category_rects.append((rect, category))
                pygame.draw.rect(screen, category_colors[category], rect, border_radius=20)
                category_surface = answer_font.render(category, True, TEXT_COLOR)
            else:
                pygame.draw.rect(screen, "grey", rect, border_radius=20)
                category_surface = answer_font.render(category, True, "darkgrey")
            
            category_surface_rect = category_surface.get_rect(center=(x + 226 // 2, y + 75 // 2))
            screen.blit(category_surface, category_surface_rect)

        x = 2 * 226 + 2 * 20 + 41
        y = 6 * 75 + 100 + 6 * 10
        random_rect = pygame.Rect(x, y, 226, 75)
        category_rects.append((random_rect, "R"))
        pygame.draw.rect(screen, category_colors["Random"], random_rect, border_radius=20)
        random_surface = answer_font.render("Random", True, TEXT_COLOR)
        random_surface_rect = random_surface.get_rect(center=(x + 226 // 2, y + 75 // 2))
        screen.blit(random_surface, random_surface_rect)

    if game_state == "question":
        y = 50
        answer_rects = []
        lines = wrap_text(current_question["question"], question_font, 750)
        for line in lines:
            player_question_surface = question_font.render(line, True, TEXT_COLOR)
            player_question_surface_rect = player_question_surface.get_rect(center=(400, y))
            y += 40
            screen.blit(player_question_surface, player_question_surface_rect)
        
        for i, c in enumerate(current_question["choices"], 1):
            answer_rect = pygame.Rect(150, 160 + (i * 80), 500, 60)
            answer_rects.append((answer_rect, i - 1))
            pygame.draw.rect(screen, category_colors[current_category], answer_rect, border_radius=10)
            answer_surface_c = answer_font.render(c, True, TEXT_COLOR)
            answer_surface_c_rect = answer_surface_c.get_rect(center=answer_rect.center)
            screen.blit(answer_surface_c, answer_surface_c_rect)
    
    if game_state == "feedback":
        y = 50
        feedback_lines = wrap_text(feedback_text, font, 700)
        for feedback_line in feedback_lines:
            feedback_line_surface = font.render(feedback_line, True, TEXT_COLOR)
            feedback_line_surface_rect = feedback_line_surface.get_rect(center=(400, y))
            screen.blit(feedback_line_surface, feedback_line_surface_rect)
            y += 40

        player_score_surface = font.render(f"Score: {player_score}", True, TEXT_COLOR)
        player_score_surface_rect = player_score_surface.get_rect(center=(400, y + 20))
        screen.blit(player_score_surface, player_score_surface_rect)

        correct_answers_surface = font.render(f"Correct Answers: {correct_answers}", True, TEXT_COLOR)
        correct_answers_surface_rect = correct_answers_surface.get_rect(center=(400, y + 70))
        screen.blit(correct_answers_surface, correct_answers_surface_rect)

        incorrect_answers_surface = font.render(f"Incorrect Answers: {incorrect_answers}", True, TEXT_COLOR)
        incorrect_answers_surface_rect = incorrect_answers_surface.get_rect(center=(400, y + 120))
        screen.blit(incorrect_answers_surface, incorrect_answers_surface_rect)

        enter_surface = font.render("Click to Continue", True, TEXT_COLOR)
        enter_surface_rect = enter_surface.get_rect(center=(400, 400))
        screen.blit(enter_surface, enter_surface_rect)

    if game_state == "win":
        you_win_surface = font.render(f"{player_name.title()} Wins!", True, TEXT_COLOR)
        you_win_surface_rect = you_win_surface.get_rect(center=(400, 75))
        screen.blit(you_win_surface, you_win_surface_rect)

        score_surface = font.render(f"Final Score: {player_score}", True, TEXT_COLOR)
        score_surface_rect = score_surface.get_rect(center=(400, 175))
        screen.blit(score_surface, score_surface_rect)

        correct_surface = font.render(f"Correct: {correct_answers}", True, TEXT_COLOR)
        correct_surface_rect = correct_surface.get_rect(center=(400, 250))
        screen.blit(correct_surface, correct_surface_rect)

        incorrect_surface = font.render(f"Incorrect: {incorrect_answers}", True, TEXT_COLOR)
        incorrect_surface_rect = incorrect_surface.get_rect(center=(400, 325))
        screen.blit(incorrect_surface, incorrect_surface_rect)

        pygame.draw.rect(screen, BUTTON_COLOR, play_again_rect, border_radius=10)
        play_again_surface = font.render("Play Again", True, TEXT_COLOR)
        play_again_surface_rect = play_again_surface.get_rect(center=play_again_rect.center)
        screen.blit(play_again_surface, play_again_surface_rect)

        pygame.draw.rect(screen, BUTTON_COLOR, exit_rect, border_radius=10)
        exit_surface = font.render("Exit", True, TEXT_COLOR)
        exit_surface_rect = exit_surface.get_rect(center=exit_rect.center)
        screen.blit(exit_surface, exit_surface_rect)

    pygame.display.flip()
    clock.tick(60)

# Welcome
# Game length
# Player difficulty (Fixed or Mixed)
# Fixed difficulty (if Fixed chosen)
# Mixed difficulty (before each question, if Mixed chosen)
# Category mode (Random or Choose)
# Question
# Feedback
# Win