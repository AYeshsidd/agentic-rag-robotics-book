import pytest
from ..main import extract_text_from_html

def test_extract_text_from_html():
    """
    Tests that the extract_text_from_html function correctly extracts text
    from the <article> tag and ignores other content.
    """
    sample_html = """
    <html>
        <head><title>Test Page</title></head>
        <body>
            <header>This is the header</header>
            <nav>Navigation links</nav>
            <main>
                <article>
                    <h1>This is the article title</h1>
                    <p>This is the first paragraph.</p>
                    <p>This is the second paragraph.</p>
                </article>
            </main>
            <footer>This is the footer</footer>
        </body>
    </html>
    """
    
    expected_text = "This is the article title This is the first paragraph. This is the second paragraph."
    actual_text = extract_text_from_html(sample_html)
    
    assert actual_text == expected_text

def test_extract_text_from_html_no_article():
    """
    Tests that the function returns an empty string if no <article> tag is found.
    """
    sample_html = """
    <html>
        <body>
            <main>
                <div>Some other content</div>
            </main>
        </body>
    </html>
    """
    
    actual_text = extract_text_from_html(sample_html)
    assert actual_text == ""
