"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [
                [1, 2, 3, 4, 5],
                [1, 1, 1, 2, 3],
                [1, 1, 1, 2, 2],
                [1, 2, 2, 2, 1],
                [1, 1, 1, 1, 1]
            ],
            "answer": [14, 1],
            "explanation": [
                [1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0],
                [1, 1, 1, 0, 0],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1]
            ]
        },
        {
            "input": [
                [2, 1, 2, 2, 2, 4],
                [2, 5, 2, 2, 2, 2],
                [2, 5, 4, 2, 2, 2],
                [2, 5, 2, 2, 4, 2],
                [2, 4, 2, 2, 2, 2],
                [2, 2, 4, 4, 2, 2]
            ],
            "answer": [19, 2],
            "explanation": [
                [0, 0, 2, 2, 2, 0],
                [0, 0, 2, 2, 2, 2],
                [0, 0, 0, 2, 2, 2],
                [0, 0, 2, 2, 0, 2],
                [0, 0, 2, 2, 2, 2],
                [0, 0, 0, 0, 2, 2]
            ]
        },
        {
            "input": [
                [4, 4, 4, 4, 4, 3, 4],
                [2, 3, 4, 4, 4, 4, 4],
                [2, 4, 4, 5, 4, 4, 3],
                [4, 2, 2, 4, 1, 2, 4],
                [3, 4, 1, 4, 4, 4, 5],
                [4, 4, 2, 4, 4, 2, 4],
                [3, 4, 4, 4, 4, 4, 2]
            ],
            "answer": [15, 4],
            "explanation": [
                [4, 4, 4, 4, 4, 0, 4],
                [0, 0, 4, 4, 4, 4, 4],
                [0, 4, 4, 0, 4, 4, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]
            ]
        },
        {
            "input": [
                [4, 4, 2, 3, 1, 5],
                [5, 5, 5, 1, 2, 2],
                [1, 3, 4, 4, 1, 1],
                [3, 3, 1, 4, 4, 4],
                [4, 5, 2, 3, 2, 4],
                [2, 2, 1, 3, 2, 2]
            ],
            "answer": [6, 4],
            "explanation": [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 4, 4, 0, 0],
                [0, 0, 0, 4, 4, 4],
                [0, 0, 0, 0, 0, 4],
                [0, 0, 0, 0, 0, 0]
            ]
        },
        {
            "input": [
                [5, 5, 4, 1, 2, 4, 4, 4],
                [2, 2, 4, 5, 4, 5, 4, 5],
                [2, 4, 4, 1, 5, 2, 3, 4],
                [4, 1, 2, 4, 2, 3, 1, 2],
                [5, 3, 2, 1, 5, 2, 3, 3],
                [4, 3, 4, 3, 5, 5, 5, 5],
                [5, 4, 2, 5, 5, 5, 5, 2],
                [3, 4, 3, 5, 1, 3, 1, 2]
            ],
            "answer": [10, 5],
            "explanation": [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 5, 0, 0, 0],
                [0, 0, 0, 0, 5, 5, 5, 5],
                [0, 0, 0, 5, 5, 5, 5, 0],
                [0, 0, 0, 5, 0, 0, 0, 0]
            ]
        },
        {
            "input": [
                [4, 2, 5, 5, 1, 4],
                [4, 4, 5, 3, 4, 1],
                [2, 5, 4, 1, 5, 4],
                [1, 3, 1, 2, 2, 4],
                [5, 3, 4, 2, 5, 2],
                [4, 5, 5, 5, 5, 2]
            ],
            "answer": [5, 5],
            "explanation": [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 5, 0],
                [0, 5, 5, 5, 5, 0]
            ]
        },
        {
            "input": [
                [5, 1, 5],
                [5, 5, 5],
                [5, 3, 2]
            ],
            "answer": [6, 5],
            "explanation": [
                [5, 0, 5],
                [5, 5, 5],
                [5, 0, 0]
            ]
        },
        {
            "input": [
                [5, 5, 2, 5, 3],
                [4, 2, 4, 5, 2],
                [4, 4, 5, 5, 4],
                [2, 2, 5, 1, 3],
                [5, 5, 5, 1, 4]
            ],
            "answer": [8, 5],
            "explanation": [
                [0, 0, 0, 5, 0],
                [0, 0, 0, 5, 0],
                [0, 0, 5, 5, 0],
                [0, 0, 5, 0, 0],
                [5, 5, 5, 0, 0]
            ]
        },
        {
            "input": [
                [1, 1, 5, 1, 1, 4, 2],
                [2, 4, 3, 2, 3, 4, 5],
                [1, 5, 4, 4, 4, 1, 1],
                [1, 4, 4, 2, 5, 1, 3],
                [4, 4, 1, 1, 1, 5, 3],
                [4, 2, 1, 3, 5, 3, 3],
                [4, 5, 2, 1, 4, 5, 5]
            ],
            "answer": [9, 4],
            "explanation": [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 4, 4, 4, 0, 0],
                [0, 4, 4, 0, 0, 0, 0],
                [4, 4, 0, 0, 0, 0, 0],
                [4, 0, 0, 0, 0, 0, 0],
                [4, 0, 0, 0, 0, 0, 0]
            ]
        }

    ],
    "Extra": [
        {
            "input": [
                [2, 5, 3, 3, 3, 3, 3, 4, 4],
                [1, 4, 1, 3, 4, 1, 3, 4, 1],
                [5, 2, 4, 5, 4, 5, 4, 1, 4],
                [3, 2, 2, 4, 1, 5, 2, 2, 5],
                [5, 4, 1, 4, 2, 5, 2, 1, 5],
                [1, 2, 5, 2, 4, 3, 2, 1, 2],
                [3, 2, 1, 4, 1, 1, 2, 5, 4],
                [4, 1, 4, 5, 3, 5, 4, 2, 2],
                [5, 4, 3, 4, 4, 1, 1, 5, 3]
            ],
            "answer": [7, 3],
            "explanation": [
                [0, 0, 3, 3, 3, 3, 3, 0, 0],
                [0, 0, 0, 3, 0, 0, 3, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        },
        {
            "input": [
                [3, 4, 1, 1, 4, 5, 5, 5, 4, 2],
                [2, 1, 5, 1, 3, 5, 4, 4, 2, 4],
                [3, 2, 2, 4, 5, 4, 2, 5, 4, 5],
                [3, 1, 5, 5, 3, 5, 2, 5, 2, 5],
                [1, 3, 5, 4, 2, 3, 1, 5, 2, 5],
                [5, 3, 4, 4, 3, 4, 5, 2, 4, 1],
                [2, 5, 5, 4, 4, 2, 3, 5, 4, 4],
                [3, 2, 5, 3, 4, 3, 3, 2, 4, 1],
                [5, 3, 1, 5, 1, 3, 4, 1, 1, 2],
                [4, 2, 3, 1, 4, 4, 1, 3, 2, 3]
            ],
            "answer": [6, 4],
            "explanation": [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
                [0, 0, 4, 4, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 4, 4, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 4, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        },
        {
            "input": [
                [4, 4, 2, 3, 5, 4],
                [2, 4, 1, 5, 2, 5],
                [5, 3, 4, 1, 1, 3],
                [5, 2, 1, 3, 4, 1],
                [4, 2, 4, 3, 4, 3],
                [1, 3, 4, 4, 4, 3]
            ],
            "answer": [6, 4],
            "explanation": [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 4, 0],
                [0, 0, 4, 0, 4, 0],
                [0, 0, 4, 4, 4, 0]
            ]
        },
        {
            "input": [
                [4, 2, 4, 5, 3, 5, 4, 3, 3],
                [2, 4, 2, 4, 3, 2, 2, 2, 5],
                [3, 3, 3, 1, 2, 1, 2, 4, 3],
                [1, 3, 5, 5, 2, 4, 2, 3, 5],
                [1, 5, 1, 1, 3, 4, 4, 4, 4],
                [4, 1, 4, 4, 5, 5, 4, 3, 5],
                [2, 4, 4, 2, 5, 5, 1, 1, 4],
                [3, 3, 3, 1, 1, 4, 2, 1, 2],
                [2, 4, 2, 3, 2, 4, 2, 2, 5]
            ],
            "answer": [6, 4],
            "explanation": [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 4, 0, 0, 0],
                [0, 0, 0, 0, 0, 4, 4, 4, 4],
                [0, 0, 0, 0, 0, 0, 4, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        },
        {
            "input": [
                [5, 4, 1, 4, 5, 5, 2, 4, 5, 4],
                [2, 3, 2, 1, 1, 3, 4, 4, 5, 5],
                [5, 4, 5, 5, 2, 3, 3, 1, 1, 4],
                [1, 4, 4, 2, 4, 2, 3, 3, 5, 4],
                [3, 5, 4, 5, 5, 5, 5, 4, 3, 4],
                [3, 5, 3, 1, 3, 5, 3, 1, 5, 5],
                [1, 4, 1, 2, 5, 5, 2, 3, 2, 1],
                [2, 2, 3, 4, 4, 3, 3, 5, 2, 5],
                [1, 2, 4, 2, 1, 1, 5, 1, 3, 1],
                [1, 2, 4, 3, 3, 4, 4, 2, 5, 2]
            ],
            "answer": [7, 5],
            "explanation": [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 5, 5, 5, 5, 0, 0, 0],
                [0, 0, 0, 0, 0, 5, 0, 0, 0, 0],
                [0, 0, 0, 0, 5, 5, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        },
        {
            "input": [
                [4, 1, 1, 2, 3, 3, 3],
                [3, 1, 4, 1, 2, 1, 3],
                [2, 1, 1, 1, 3, 3, 4],
                [3, 2, 4, 1, 5, 2, 1],
                [5, 1, 4, 5, 3, 5, 3],
                [5, 2, 5, 4, 2, 2, 4],
                [5, 3, 5, 3, 4, 1, 4]
            ],
            "answer": [8, 1],
            "explanation": [
                [0, 1, 1, 0, 0, 0, 0],
                [0, 1, 0, 1, 0, 0, 0],
                [0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]
            ]
        },
        {
            "input": [
                [4, 5, 5, 3, 4, 1, 5, 1],
                [5, 3, 2, 1, 1, 1, 1, 3],
                [4, 3, 1, 1, 3, 4, 4, 2],
                [2, 4, 4, 5, 4, 2, 4, 4],
                [2, 1, 5, 3, 5, 4, 5, 4],
                [2, 3, 4, 5, 3, 2, 3, 4],
                [3, 3, 4, 2, 4, 5, 5, 2],
                [1, 2, 2, 2, 1, 3, 5, 5]
            ],
            "answer": [7, 1],
            "explanation": [
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 1, 1, 1, 0],
                [0, 0, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]
            ]
        },
        {
            "input": [
                [3, 3, 1, 3, 3],
                [4, 3, 5, 1, 1],
                [3, 4, 5, 5, 3],
                [3, 5, 5, 1, 5],
                [1, 5, 5, 2, 5]
            ],
            "answer": [7, 5],
            "explanation": [
                [0, 0, 0, 0, 0],
                [0, 0, 5, 0, 0],
                [0, 0, 5, 5, 0],
                [0, 5, 5, 0, 0],
                [0, 5, 5, 0, 0]
            ]
        },
        {
            "input": [
                [1, 5, 1, 5, 4, 1, 5, 4, 4],
                [5, 5, 2, 3, 2, 3, 3, 1, 1],
                [2, 2, 3, 3, 5, 5, 4, 3, 3],
                [2, 5, 1, 2, 2, 4, 3, 3, 2],
                [2, 2, 5, 2, 4, 4, 5, 1, 1],
                [5, 5, 1, 5, 4, 2, 2, 5, 3],
                [3, 2, 1, 1, 3, 4, 2, 3, 1],
                [3, 4, 3, 3, 5, 5, 2, 2, 2],
                [1, 2, 4, 5, 5, 3, 3, 2, 1]
            ],
            "answer": [7, 2],
            "explanation": [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 2, 2, 0, 0],
                [0, 0, 0, 0, 0, 0, 2, 0, 0],
                [0, 0, 0, 0, 0, 0, 2, 2, 2],
                [0, 0, 0, 0, 0, 0, 0, 2, 0]
            ]
        },
        {
            "input": [
                [4, 2, 4, 3, 1, 3, 1, 2],
                [4, 5, 3, 5, 5, 5, 5, 4],
                [2, 5, 3, 3, 3, 4, 4, 4],
                [2, 2, 2, 4, 4, 1, 4, 4],
                [1, 3, 4, 5, 1, 1, 1, 2],
                [1, 2, 5, 5, 2, 5, 1, 2],
                [4, 1, 2, 5, 3, 1, 3, 3],
                [4, 1, 4, 3, 5, 1, 4, 4]
            ],
            "answer": [6, 4],
            "explanation": [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 4],
                [0, 0, 0, 0, 0, 4, 4, 4],
                [0, 0, 0, 0, 0, 0, 4, 4],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]
            ]
        },
        {
            "input": [
                [3, 3, 2, 4, 5, 5, 1, 5, 3, 3],
                [5, 3, 5, 2, 2, 4, 4, 3, 3, 4],
                [3, 5, 3, 4, 4, 2, 2, 1, 4, 5],
                [4, 1, 3, 1, 3, 5, 3, 2, 1, 3],
                [5, 2, 5, 2, 3, 4, 1, 4, 4, 4],
                [5, 2, 5, 3, 1, 5, 4, 5, 3, 2],
                [5, 1, 5, 5, 5, 5, 5, 2, 2, 3],
                [2, 2, 3, 3, 4, 3, 1, 2, 3, 2],
                [3, 1, 2, 4, 4, 4, 1, 3, 1, 4],
                [4, 2, 2, 1, 5, 1, 2, 5, 3, 2]
            ],
            "answer": [8, 5],
            "explanation": [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 5, 0, 0, 5, 0, 0, 0, 0],
                [0, 0, 5, 5, 5, 5, 5, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        },
        {
            "input": [
                [5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5],
            ],
            "answer": [25, 5],
            "explanation": [
                [5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5],
                [5, 5, 5, 5, 5],
            ]
        },
        {
            "input": [
                [5, 5, 5, 5, 5],
                [5, 1, 2, 1, 5],
                [5, 2, 5, 2, 5],
                [5, 1, 2, 1, 5],
                [5, 5, 5, 5, 5],
            ],
            "answer": [16, 5],
            "explanation": [
                [5, 5, 5, 5, 5],
                [5, 0, 0, 0, 5],
                [5, 0, 0, 0, 5],
                [5, 0, 0, 0, 5],
                [5, 5, 5, 5, 5],
            ]
        },


    ]
}
