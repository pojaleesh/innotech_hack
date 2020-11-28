import src.from_pdf_to_text
import src.get_pdf

# Требуется Google Chrome
# Установить ChromeDriver соответсвующей версии Google Chrome в C:/Program Files/chromedriver/ 
# В архивах в папке src для каждой OS ChromeDriver версии 86.0.4240.22 

def get_pdf(name_or_id):
    src.get_pdf.get_pdf(name_or_id)
    return src.from_pdf_to_text.make_data(src.from_pdf_to_text.from_pdf_to_text())
    
def main():
    return get_pdf('773370633582')

if __name__ == '__main__':
    print(main())