from scrapegraphai.graphs import SmartScraperGraph
GOOGLE_APIKEY = "YOUR_API_KEY"

# Define the configuration for the graph
graph_config = {
    "llm": {
        "api_key": GOOGLE_APIKEY,
        "model": "gemini-pro",
    },
}

# Create the SmartScraperGraph instance
smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the quotes, authors and tags ",
    file_source="http://quotes.toscrape.com",  # also accepts a string with the already downloaded HTML code as string format
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)