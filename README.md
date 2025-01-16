```markdown
# Vesta Equity FAQ Assistant 🏠

This project provides a streamlined solution for navigating Vesta Equity's FAQ page by leveraging a custom-built Q&A system. The system uses advanced AI models, embeddings, and a vector database to deliver accurate and efficient answers to user queries. By eliminating the need to manually search through multiple categories, this tool saves time and improves user experience.

---

## Features 🚀

- **Efficient Query Resolution**: Quickly fetch answers to specific questions without browsing through the entire FAQ page.
- **Powered by AI**: Utilizes OpenAI's powerful LLM for natural language understanding and response generation.
- **Custom Embeddings**: Employs the `InstructorEmbedding` model for precise document similarity calculations.
- **FAISS Vector Database**: Stores and retrieves documents efficiently, enabling fast and accurate question answering.
- **Streamlit Interface**: Simple and interactive web interface for user interaction.
- **Customizable**: Easy to extend with new questions and answers or adapt for other datasets.

---

## Technology Stack 🛠️

- **Language Model**: [OpenAI](https://openai.com/)
- **Embeddings**: [HuggingFace Instructor Embeddings](https://huggingface.co/hkunlp/instructor-base)
- **Vector Database**: [FAISS](https://faiss.ai/)
- **Frameworks**:
  - [LangChain](https://www.langchain.com/)
  - [Streamlit](https://streamlit.io/)
- **Dataset**: FAQ dataset created from Vesta Equity's FAQ page.

---

## Installation 🛠️

### Prerequisites
- Python 3.10 or higher
- OpenAI API Key
- Required Python packages (listed in `requirements.txt`)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/vesta-equity-faq-assistant.git
   cd vesta-equity-faq-assistant
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```
---

## Usage 💻

### Streamlit Web App
1. Launch the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Use the interface to:
   - Process FAQs by clicking the "Process FAQs" button.
   - Enter a question in the text input field to get an answer.

---

## How It Works 🧠

1. **Data Processing**:
   - `faqs.csv` is loaded and processed using LangChain's `CSVLoader`.
   - Each FAQ is embedded into a vector space using HuggingFace's `InstructorEmbedding`.

2. **Vector Database**:
   - The FAQs are stored in a FAISS vector database for efficient retrieval.
   - The database is queried using cosine similarity to find the most relevant answers.

3. **Response Generation**:
   - OpenAI's LLM generates detailed answers based on the retrieved context.
   - The response adheres closely to the FAQ dataset, ensuring accurate and trustworthy answers.

4. **Streamlit Interface**:
   - A user-friendly web interface allows easy interaction, including FAQ processing and question answering.

---

## Example Dataset (`faqs.csv`) 📂

| **prompt**                           | **response**                                                                                                                                       |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------| | Does Vesta Equity Provide Loans?     | There is no lending on Vesta Equity. Property owners can list a portion of equity they want to sell by setting a percentage and a desired amount    |                                      | that accredited investors can negotiate and purchase. Once the transaction is approved by Vesta Equity, the investor fully owns the equity they’ve   |                                      | purchased and the property owner receives the negotiated funds. These funds belong to the property owner who can use them at their own discretion.  |
| What is Vesta Equity?                | Vesta Equity provides solutions for home equity and real estate investment. |

---

## Benefits 🌟

- **Time-Saving**: Quickly answers specific questions without searching through multiple categories.
- **Accurate**: Leverages advanced embeddings and AI for precise context-based answers.
- **Scalable**: Easily extendable to other FAQs or datasets.

---

## License 📄
This project is licensed under the MIT License. See the `LICENSE` file for details.
