import mammoth

with open("sample.docx", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value # The generated HTML
    messages = result.messages # Any messages, such as warnings during conversion
    print(messages)

# from markitdown import MarkItDown

# md = MarkItDown() # Set to True to enable plugins
# result = md.convert("result.docx")
# print(result.text_content)