import os
from typing import List, Dict

from dotenv import load_dotenv
from openai import OpenAI


def build_input(messages: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """Transform local history into Responses API input format."""
    return [{"role": msg["role"], "content": msg["content"]} for msg in messages]


def main() -> None:
    load_dotenv(".env")
    load_dotenv(".env.test")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit(
            "Falta OPENAI_API_KEY. Define la variable en .env o .env.test."
        )

    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    client = OpenAI(api_key=api_key)

    print("Chat listo. Escribe 'salir' para terminar.\n")

    history: List[Dict[str, str]] = [
        {
            "role": "system",
            "content": (
                "Actua como un amigo cercano: amable, paciente y directo. "
                "Responde en espanol claro, con tono natural y breve."
            ),
        }
    ]

    while True:
        user_text = input("Tu: ").strip()
        if user_text.lower() in {"salir", "exit", "quit"}:
            print("Hasta luego.")
            break

        if not user_text:
            continue

        history.append({"role": "user", "content": user_text})

        response = client.responses.create(
            model=model,
            input=build_input(history),
        )
        assistant_text = response.output_text.strip()
        print(f"Amigo: {assistant_text}\n")

        history.append({"role": "assistant", "content": assistant_text})


if __name__ == "__main__":
    main()
