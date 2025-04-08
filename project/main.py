def render_page():
    with open('templates/customer_add.html', 'r') as file:
        html_content = file.read()
    return html_content

if __name__ == "__main__":
    page_content = render_page()
    print(page_content)  # This will print the HTML content to the console
