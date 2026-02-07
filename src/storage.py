"""
Data persistence module for activities storage.

Handles loading and saving activities to JSON files,
providing a simple file-based data storage solution.
"""

import json
import logging
from pathlib import Path
from typing import Dict, Any

# Configure logging
logger = logging.getLogger(__name__)

# Data file location
DATA_FILE = Path(__file__).parent / "activities.json"


def load_activities() -> Dict[str, Any]:
    """
    Load activities from the JSON file.
    
    Returns:
        Dictionary of activities loaded from file.
        Returns empty dict if file doesn't exist.
    
    Raises:
        json.JSONDecodeError: If JSON file is malformed
    """
    try:
        if DATA_FILE.exists():
            with open(DATA_FILE, 'r') as f:
                activities = json.load(f)
                logger.info(f"Loaded {len(activities)} activities from {DATA_FILE}")
                return activities
        else:
            logger.warning(f"Data file not found at {DATA_FILE}")
            return {}
    except json.JSONDecodeError as e:
        logger.error(f"Error parsing JSON file: {e}")
        raise
    except Exception as e:
        logger.error(f"Error loading activities: {e}")
        raise


def save_activities(activities: Dict[str, Any]) -> None:
    """
    Save activities to the JSON file.
    
    Args:
        activities: Dictionary of activities to save
    
    Raises:
        IOError: If unable to write to file
    """
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(activities, f, indent=2)
            logger.info(f"Saved {len(activities)} activities to {DATA_FILE}")
    except IOError as e:
        logger.error(f"Error saving activities: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error saving activities: {e}")
        raise
