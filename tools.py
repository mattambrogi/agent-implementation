import httpx

def wikipedia(q):
  """ 
  wikipedia:
  e.g. wikipedia: Django
  Returns a summary from searching Wikipedia
  """
  return httpx.get("https://en.wikipedia.org/w/api.php", params={
      "action": "query",
      "list": "search",
      "srsearch": q,
      "format": "json"
  }).json()["query"]["search"][0]["snippet"]


def simon_blog_search(q):
  """
  simon_blog_search:
  e.g. simon_blog_search: Django
  Search Simon's blog for that term
  """
  results = httpx.get("https://datasette.simonwillison.net/simonwillisonblog.json", params={
      "sql": """
      select
        blog_entry.title || ': ' || substr(html_strip_tags(blog_entry.body), 0, 1000) as text,
        blog_entry.created
      from
        blog_entry join blog_entry_fts on blog_entry.rowid = blog_entry_fts.rowid
      where
        blog_entry_fts match escape_fts(:q)
      order by
        blog_entry_fts.rank
      limit
        1""".strip(),
      "_shape": "array",
      "q": q,
  }).json()
  return results[0]["text"]

def calculate(what):
  """
  calculate:
  e.g. calculate: 4 * 7 / 3
  Runs a calculation and returns the number - uses Python so be sure to use floating point syntax if     necessary
  """
  return eval(what)

def fetch_last_todo(input=None):
  """
  fetch_last_todo:
  e.g. fetch_last_todo: none
  Returns the last todo item from the fetched todos list. No input required.
  """
  url = "https://jsonplaceholder.typicode.com/todos/1"
  response = httpx.get(url)

  if response.status_code == 200:
    print(response.json())
    return response.json()
  else:
    print('failed')
    return "Failed to fetch data"