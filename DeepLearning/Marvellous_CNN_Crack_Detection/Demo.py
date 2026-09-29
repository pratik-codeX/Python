import requests
from bs4 import BeautifulSoup


def print_secret_message(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    rows = []

    for tr in soup.find_all("tr"):
        cells = tr.find_all(["td", "th"])

        if len(cells) >= 3:
            values = [cell.get_text(strip=True) for cell in cells]

            try:
                x = int(values[0])
                character = values[1]
                y = int(values[2])

                rows.append((x, y, character))
            except ValueError:
                continue

    if not rows:
        print("No data found")
        return

    max_x = max(x for x, y, char in rows)
    max_y = max(y for x, y, char in rows)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, character in rows:
        grid[max_y - y][x] = character

    for row in grid:
        print("".join(row))


url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"

print_secret_message(url)