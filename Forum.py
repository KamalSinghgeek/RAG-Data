import requests
from bs4 import BeautifulSoup

def extract_qna_from_fleetstack_topic(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Error fetching page: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Example selectors based on actual site structure
    question = soup.find('h1')  # Assuming main <h1> is the question
    answer_block = soup.find('div', class_='post-content')  # The actual answer

    question_text = question.get_text(strip=True) if question else "Question not found"
    answer_text = answer_block.get_text(separator='\n', strip=True) if answer_block else "Answer not found"

    with open('qna_output.txt', 'w', encoding='utf-8') as f:
        f.write(f"Q: {question_text}\n\nA: {answer_text}\n")

    print("✅ Q&A extracted and saved to qna_output.txt")


# Run for the provided URL
extract_qna_from_fleetstack_topic("https://fleetstackglobal.com/topic/-Do-I-get-the-source-code-or-is-it")
