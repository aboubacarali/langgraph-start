from graph_builder import build_graph


def main():
    app = build_graph()

    user_question = input("Pose ta question : ")

    result = app.invoke({
        "question": user_question,
        "category": "",
        "answer": ""
    })

    print("\nRéponse finale :")
    print(result["answer"])


if __name__ == "__main__":
    main()
