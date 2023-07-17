"""Module containing functions with lists of switches
for connection, as well as lists of buildings for various
functions."""

def crit_buildings():
    """List of buildings deemed 'critical'."""
    buildings = [
        crit_switches()
        ]
    return buildings


def interface_buildings():
    """List of all buildings, both critical and not."""
    buildings = [
        crit_switches(),
        non_crit_switches()
        ]
    return buildings


def crit_switches():
    """All critical switches in Example Building"""
    v_crit_switches = [
        "exampleswitch1",
        "exampleswitch2",
        "examplerouter1",
        "examplerouter2",
        "exampledistrt1",
        "examplecorert2"
        ]
    return v_crit_switches


def non_crit_switches():
    """All non-critical switches in Example Building"""
    v_non_crit_switches_2 = [
        "exampleswitch1",
        "exampleswitch2",
        "examplerouter1",
        "examplerouter2",
        "exampledistrt1",
        "examplecorert2"
        ]
    return v_non_crit_switches_2
