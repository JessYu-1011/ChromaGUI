This is the English version of the README for your project. I have ensured that no emojis are used, and I will maintain this style for all future programming tasks.

---

# ChromaDB Flask GUI

This is a lightweight web interface for managing remote ChromaDB instances. It is specifically designed to handle Cloudflare Access authentication and utilizes a Flask proxy to bypass browser CORS restrictions.

## Features

1. Stores connection settings, including Cloudflare Service Tokens, via browser cookies.
2. Visualizes all available Collections.
3. Provides detailed views of IDs, documents, and metadata within specific Collections.
4. Automatically maintains compatibility with both ChromaDB v1 and v2 API requests.

## Requirements

Ensure your environment is running Python 3.8 or higher. Install the necessary dependencies using the following command:

```bash
pip install flask chromadb pandas

```

## Usage

1. Clone or copy this repository to your local machine.
2. Run the application:
```bash
python app.py

```


3. Open your browser and navigate to `http://127.0.0.1:5001`.
4. Enter your remote host address, port, and Cloudflare Service Token (Client-Id and Client-Secret) on the setup page.
5. Save the settings to begin managing your vector data.

## Project Structure

* `app.py`: The main Flask backend application.
* `templates/`: Directory containing HTML templates.
* `setup.html`: Connection configuration page.
* `index.html`: Collection list dashboard.
* `collection.html`: Detailed data view for specific collections.



## Security Considerations

* Connection details, including the Client-Secret, are stored as plain text in your local browser cookies. Only use this application on trusted devices.
* It is recommended to run this interface within a private or protected network environment.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Would you like me to help you refine the CSS to make the interface look more professional, or shall we move on to adding search functionality?