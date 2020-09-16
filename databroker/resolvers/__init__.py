
from urllib.parse import urlparse

from databroker.resolvers.file import FileResolver
from databroker.exceptions import BadRequestError,VariableNotFound

RESOLVERS = {
        "file":FileResolver,
}

def getResolver(uri):
    scheme = urlparse(uri).scheme
    try:
        return RESOLVERS[scheme](uri)
    except KeyError:
        raise NotImplementedError(f"Scheme \"{scheme}\" not implemented")

def resolve(query,sources):
    try:
        sources = sources[query["loa"]]
    except KeyError:
        raise BadRequestError

    data = None
    for _,uri in sources.items():
        resolver = getResolver(uri)
        try:
            data=resolver.get(query["variable"])
        except VariableNotFound:
            pass
    return data 

