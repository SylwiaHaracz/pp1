import mymath
import mykeyboard

randomowy = mymath.generate_number()
keyboard = mykeyboard.read_number()
print(f"Computer's number:{randomowy}")
if randomowy == keyboard:
    print("You won the game!")
else:
    print("You're wrong :(")