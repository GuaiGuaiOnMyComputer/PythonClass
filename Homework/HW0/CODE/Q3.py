from Q2 import try_parse_input

def output_result(bmi):
    if bmi < 18.5:
        print(f"Your bmi is {bmi:.3f} Too skinny.")
    elif bmi >= 18.5 and bmi < 24:
        print(f"Your bmi is {bmi:.3f} Healthy build")
    else:
        print(f"Your bmi is {bmi:.3f} Overweight")

def main():
    stats = {
        "Weight": 0,
        "Height": 0
    }
    bmi = 0
    for _ in range(3):
        for key in stats:
            prompt = None
            match key:
                case "Weight":
                    prompt = "Please input your weight in kgs.\t"
                case "Height":
                    prompt = "Please input your height in meters.\t"
            stats[key] = try_parse_input(float, prompt)
        bmi = stats["Weight"] / (stats["Height"] ** 2)
        output_result(bmi)

if __name__ == "__main__":
    main()