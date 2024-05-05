def walks(steps):
    if steps == 1:
        return
    walks(steps -1)
    print(f"You take steps {steps}")


walks(100)