#TestData is package name and ImdbData is python file
class Imdbdata:
    url = "https://www.imdb.com/search/name/"
    search_data = "Shah Rukh Khan"
    start_date = "16/05/1960"
    end_date = "16/05/1998"
    class Imdblocators:
        # xpath for Imdb_page
        name_locator = "//label//span[1]//div[text()='Name']"
        name_search_box_locator = "//div[@class='ipc-textfield__container']//input[@placeholder='e.g. Robert Wolders']"
        Birth_date_locator = "//label//span//div[text()='Birth date']"
        result_locator = "//button//span[text()='See results']"
        start_date_locator = "//input[@data-testid='birthDate-start']"
        end_date_locator = "//input[@data-testid='birthDate-end']"
        search_data = "Shah Rukh Khan"
        start_date = "16/05/1960"
        end_date = "16/05/1998"
        actor_locator = "//div[@data-testid='nlib-title']"

        

