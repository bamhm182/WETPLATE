import json
from uuid import uuid4
from classes.org import Org
import os


def read_orgs():
    for f in ["orgs", "example_orgs"]:
        curr = f"{f}.json"
        if os.path.exists(curr):
            break
    with open(curr) as file:
        return parse_orgs(json.loads(file.read())['orgs'])


def parse_orgs(orgs):
    ret = []
    for o in orgs:
        children = parse_orgs(o['children']) if 'children' in o.keys() else None
        children = [children] if type(children) == Org else children
        ret.append(Org(uuid4().hex.upper(), o['name'], o['mission'], o['key_words'], o['location'], children))
    return ret if len(ret) > 1 else ret[0]


def build_answer_key(curr):
    ret = dict()
    ret[curr.oid] = {'name': curr.name, 'mission': curr.mission, 'key_words': curr.key_words,
                     'location': curr.location}
    if curr.children:
        for c in curr.children:
            ret.update(build_answer_key(c))
    return ret


def wipe_values(curr):
    children = []
    oid = curr.oid
    if curr.children:
        for child in curr.children:
            children.append(wipe_values(child))
    return Org(oid=oid, children=children)


def get_values(curr, value, recurse=True):
    ret = []
    values = {
        'name': curr.name,
        'mission': curr.mission,
        'key_words': curr.key_words,
        'oid': curr.oid,
        'location': curr.location
    }
    ret.append(values[value])

    if recurse:
        if curr.children:
            for child in curr.children:
                ret.extend(get_values(child, value))
    ret = list(set(ret))
    ret.sort()
    return ret if recurse else ret[0]


def get_org(orgs, oid):
    desired = None
    if orgs.oid == oid:
        desired = orgs
    if orgs.children and not desired:
        for child in orgs.children:
            ret = get_org(child, oid)
            if ret and ret.oid == oid:
                desired = ret
    return desired
