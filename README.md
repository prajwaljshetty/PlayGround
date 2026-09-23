# Playground

Playground is a CLI tool designed to make coding competitions easier to set up, run, and evaluate.

The idea is simple: the organizer prepares the competition once, and the participant receives an already-prepared environment where they can focus on solving the challenge. Playground handles the repetitive work involved in compiling, running, testing, and evaluating code.

## Organizer

The organizer starts with an empty directory.

The organizer runs:

    playground seed

`playground seed` plants the Playground environment in the current directory and enables the Playground commands needed to prepare the competition.

The organizer then configures the required challenges.

For example:

    playground configure debug
    playground configure code

During configuration, the organizer can prepare:

- Problem or challenge
- Buggy source code
- Test cases
- Supported languages
- Starter source or template
- Marks
- Evaluation rules
- Other challenge configuration

The organizer can also configure the submission endpoint:

    playground endpoint <url>

After preparing and testing the challenge, the organizer commits the setup:

    playground commit

The prepared environment can then be committed and distributed to the participants.

## Participant

The participant does **not** run `playground seed`.

They receive an already-prepared Playground environment and enter it using:

    playground enter

After entering the environment, the participant can use the commands provided for the challenge:

    playground lang
    playground judge
    playground submit

The participant can see and modify the **challenge source code**, because that is the code they are expected to work on.

However, the participant should not have access to Playground's own implementation or the organizer's private evaluation data.

This includes:

- Playground's source code
- Evaluator implementation
- Hidden test cases
- Internal evaluation logic
- Organizer-only configuration

## Evaluation

Playground handles the repetitive execution and evaluation process.

Instead of the organizer manually compiling and running every submission, Playground can handle the process:

    Compile
       ↓
    Run
       ↓
    Provide test input
       ↓
    Capture output
       ↓
    Check output
       ↓
    Calculate marks

For example, a challenge may provide a program with a series of inputs. Playground starts the participant's program, provides the required input, captures its output, and evaluates that output against the configured test cases.

The evaluator does not need to know how the participant's program is internally implemented. It only needs to know how to run the program, what input to provide, and how the resulting output should be checked.

## Challenge Source vs Playground Source

There are two different types of source code in the environment.

### Challenge Source

This is the code the participant is supposed to work on.

For a debugging challenge, this could be the intentionally buggy program provided by the organizer.

The participant must be able to:

- Read the source
- Modify the source
- Run the program
- Fix the problems
- Submit the solution

### Playground Source

This is Playground's own implementation and evaluation machinery.

The participant should not need to see or modify this.

Playground keeps the evaluation process separate from the challenge source so that the participant interacts with the challenge rather than the evaluator itself.

## Overall Flow

    ORGANIZER
        │
        ▼
    playground seed
        │
        ▼
    Prepare the challenge
        │
        ├── Problem
        ├── Source
        └── Tests
        │
        ▼
    Configure challenge
        │
        ▼
    playground endpoint
        │
        ▼
    playground commit
        │
        ▼
    Prepared Environment
        │
        ▼
    PARTICIPANT
        │
        ▼
    playground enter
        │
        ▼
    playground lang
        │
        ▼
    Work on code
        │
        ▼
    playground judge
        │
        ▼
    playground submit
        │
        ▼
    Evaluation

## Main Idea

The organizer prepares the challenge once.

The participant enters an already-prepared environment and focuses on the challenge.

Playground hides the repetitive parts of coding-event execution and evaluation behind a simple CLI, making the process easier to set up for organizers and easier to use for participants.