from rapidfuzz import process
from tools.app_registry import app_registry
from brain.alias_learner import save_alias


def match_app(target):

    target = target.lower()

    apps = list(app_registry.keys())

    match = process.extractOne(target, apps)

    if match and match[1] > 65:

        matched_app = match[0]

        if target != matched_app:
            save_alias(target, matched_app)

        return matched_app

    return target
