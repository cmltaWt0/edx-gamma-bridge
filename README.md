RG Gamification Tracking
=========================

Parse the edX tracking log, convert the events to Gamma format, and publish them to an RG Gamification storage known Gamma.


# Configuration

Add the following configuration to the lms settings:

```python
FEATURES.update({
    "RG_GAMIFICATION": {
        "ENABLED": True,
        "RG_GAMIFICATION_ENDPOINT": "https://gamma.domain.in/",
        "KEY": "key",
        "SECRET": "secret",
        "IGNORED_EVENT_TYPES": []
    }
})
```
