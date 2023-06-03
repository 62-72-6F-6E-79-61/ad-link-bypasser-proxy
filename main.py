from mitmproxy import http

domain_list = [
    "ad-maven.com",
    "adf.ly",
    "adfoc.us",
    "adshrink.it",
    "boost.ink",
    "boost.fusedgt.com",
    "letsboost.net",
    "mboost.me",
    "rekonise.com",
    "st.st",
    "social-unlock.com",
    "sub2get.com",
    "sub2unlock.com",
    "sub2unlock.net",
    "work.ink",
    "linkvertise.com",
]


def check_url(url: str) -> bool:
    if "." in url.split("/")[-1]:
        return False
    url = url.replace("https://", "")
    url = url.replace("http://", "")
    for domain in domain_list:
        if url.startswith(domain):
            return True
    return False


def request(flow: http.HTTPFlow) -> None:
    if check_url(flow.request.pretty_url):
        print(f"bypassing {flow.request.pretty_url}")
        responose = f"""
            <html>
            <head>
            <meta http-equiv="refresh" content="0; url=https://bypass.city/bypass?bypass={flow.request.pretty_url}" />
            </head>
            <body>
            <p>Redirecting to <a href="https://bypass.city/bypass?bypass={flow.request.pretty_url}">https://bypass.city/bypass?bypass={flow.request.pretty_url}</a></p>
            </body>
            </html>
            """
        flow.response = http.Response.make(
            200,  # (optional) status code
            responose.encode(),
            {"Content-Type": "text/html"},  # (optional) headers
        )
