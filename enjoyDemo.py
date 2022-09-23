from enjoyn.example import RandomWalkExample

example = RandomWalkExample(lenght=1000)
with example.time_run():
    outputs = example.output_images()

print(f"Length: {len(outputs)}, Example: {outputs[0]}")
