import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    prob_distribution = {}
    linked_pages = corpus[page]
    total_num_pages = len(corpus)

    if not linked_pages:
        for page in corpus.keys():
            prob_distribution[page] = 1 / total_num_pages
        return prob_distribution

    for page in corpus.keys():
        if page in linked_pages:
            prob_distribution[page] = damping_factor * (1 / len(linked_pages))
        else:
            prob_distribution[page] = (1 - damping_factor) * (1 / total_num_pages)
    
    return prob_distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    sample_page_rank = {}
    first_page = random.choice(list(corpus.keys()))

    page_visits = {}
    for page in corpus.keys():
        if page != first_page:
            page_visits[page] = 0
        else:
            page_visits[page] = 1
    print(page_visits)

    current_page = first_page
    for i in range(n - 1):
        prob_distribution = transition_model(corpus, current_page, damping_factor)

        pages = list(prob_distribution.keys())
        page_weights = list(prob_distribution.values())
        next_page = random.choices(pages, weights=page_weights)[0]

        page_visits[next_page] = page_visits[next_page] + 1
        current_page = next_page
    
    for page in corpus.keys():
        sample_page_rank[page] = page_visits[page] / n
    
    return sample_page_rank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_rank = {}
    for page in corpus.keys():
        page_rank[page] = 1 / len(corpus)
    
    repeat = True
    while repeat:
        new_page_rank = {}

        for page in corpus.keys():
            prev_pages = {}
            for key, values in corpus.items():
                if page in values:
                    prev_pages[key] = len(values)
            
            new_page_rank[page] = (1 - damping_factor) * (1 / len(corpus))
            for prev_page in prev_pages.keys():
                new_page_rank[page] += damping_factor * (page_rank[prev_page] / prev_pages[prev_page])
        
        repeat = False
        for page in corpus.keys():
            val_diff = abs(new_page_rank[page] - page_rank[page])

            if val_diff > 0.001:
                repeat = True
                break
        
        page_rank = new_page_rank
    
    return page_rank


if __name__ == "__main__":
    main()
