from graph_builder import build_graph
import sys


def main():
    app = build_graph()

    # Read from stdin bytes to avoid locale/encoding issues on some terminals.
    sys.stdout.write("Pose ta question : ")
    sys.stdout.flush()
    raw = sys.stdin.buffer.readline()
    user_question = raw.decode("utf-8", errors="replace").rstrip("\r\n")

    result = app.invoke({
        "question": user_question,
        "category": "",
        "answer": ""
    })

    print("\nRéponse finale :")
    print(result["answer"])


if __name__ == "__main__":
    main()
