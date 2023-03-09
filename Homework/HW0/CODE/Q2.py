def try_parse_input(obj_constructor, prompt:str) -> int:
    try:
        return obj_constructor(input(prompt))
    except ValueError:
        print("Excuse me, What? A float or integer is required.")
        return try_parse_input(obj_constructor, prompt)

def get_input(his_exercises:dict) -> None:
    for workout in his_exercises:
        prompt = f"How many minutes have he done {workout:>8}?"
        his_exercises[workout] = try_parse_input(float, prompt)

def main():
    his_exercise = {"Swimming": 0, "Cycling": 0, "Jogging": 0}
    get_input(his_exercises = his_exercise);
    for exercise in his_exercise:
        print(f"He has done {exercise:>8} for {his_exercise[exercise]/60:>8.2f} hours")
    
if __name__ == "__main__":
    main()