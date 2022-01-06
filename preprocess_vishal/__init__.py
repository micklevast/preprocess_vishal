from preprocess_vishal import utils

__version__='0.0.2'

# this is final fule
# user import and call my method from here only
def get_wordcounts(x):
    return utils._get_wordcounts(x)

def _get_charcount(x):
    return utils._get_charcount(x)

def _get_avg_wordlength(x):
    return utils._get_avg_wordlength(x)

def _get_stopwords_counts(x):
    return utils._get_stopwords_counts(x)

def _get_hashtags_counts(x):
    return utils._get_hashtags_counts(x)

def _get_mentions_counts(x):
    return utils._get_mentions_counts(x)

def _get_digit_counts(x):
    return utils._get_digit_counts(x)

def _get_uppercase_counts(x):
    return utils._get_uppercase_counts(x)

def _get_cont_to_exp(x):
    return utils._get_cont_to_exp(x)

def _get_emails(x):
    return utils._get_emails(x)

def _remove_emails(x):
    return utils._remove_emails(x)

def _get_urls(x):
    return utils._get_urls(x)

def _remove_urls(x):
    return utils._remove_urls(x)

def _remove_rt(x):
    return utils._remove_rt(x)  

def _remove_special_chars(x):
    return utils._remove_special_chars(x)

def _remove_html_tags(x):
    return utils._remove_html_tags(x)

def _remove_accented_chars(x):
    return utils._remove_accented_chars(x)

def _remove_stopwords(x):
    return utils._remove_stopwords(x)

def _make_base(x):
    return utils._make_base(x)

def _remove_common_words(x,n=20):
    return utils._remove_common_words(x)

def _remove_rarewords(x,n=20):
    return utils._remove_rarewords(x)

def _spelling_correction(x):
    return utils._spelling_correction(x)

