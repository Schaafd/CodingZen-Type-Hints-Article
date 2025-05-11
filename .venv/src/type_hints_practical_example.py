# Original version without type hints
def without_calculate_metrics(data, metric_names, normalize=False):
    results = {}

    for name in metric_names:
        if name == 'mean':
            results[name] = sum(data) / len(data)
        elif name == 'median':
            sorted_data = sorted(data)
            mid = len(sorted_data) // 2
            results[name] = sorted_data[mid]
        elif name == 'range':
            results[name] = max(data) - min(data)

    if normalize:
        max_val = max(results.values())
        for name in results:
            results[name] /= max_val

    return results

# Possible bugs:
# - What if data is empty?
# - What if metric_names contains an unsupported metric?
# - What if data contains non-numeric values?

from typing import List, Dict, Union, Optional

def with_calculate_metrics(
    data: List[float],
    metric_names: List[str],
    normalize: bool = False
) -> Dict[str, float]:
    """
    Calculate statistical metrics for a dataset.

    Args:
        data: List of numerical values to analyze
        metric_names: List of metrics to calculate (supported: 'mean', 'median', 'range')
        normalize: If True, normalize all results to be between 0 and 1

    Returns:
        Dictionary mapping metric names to their calculated values
    """
    if not data:
        raise ValueError("Cannot calculate metrics on empty data")

    valid_metrics = {'mean', 'median', 'range'}
    invalid_metrics = set(metric_names) - valid_metrics
    if invalid_metrics:
        raise ValueError(f"Unsupported metrics: {invalid_metrics}")

    results: Dict[str, float] = {}

    for name in metric_names:
        if name == 'mean':
            results[name] = sum(data) / len(data)
        elif name == 'median':
            sorted_data = sorted(data)
            mid = len(sorted_data) // 2
            results[name] = sorted_data[mid]
        elif name == 'range':
            results[name] = max(data) - min(data)

    if normalize and results:
        max_val = max(results.values())
        if max_val > 0:
            for name in results:
                results[name] /= max_val

    return results

print(f"Without type hints: {without_calculate_metrics([1, 2, 3], ['mean', 'median', 'range'])}")
print(f"With type hints: {with_calculate_metrics([1, 2, 3], ['mean', 'median', 'range'])}")