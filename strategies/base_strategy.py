from abc import ABC, abstractmethod
import pandas as pd

class BaseStrategy(ABC):
    """
    Abstract base class for trading strategies.
    All strategy implementations should inherit from this class.
    """
    
    @abstractmethod
    def generate_signals(self) -> pd.DataFrame:
        """
        Generate trading signals from market data.
        
        Returns:
        --------
        pd.DataFrame
            DataFrame containing:
            - 'signal' column with trading signals (1=long, 0=flat)
            - Indexed by datetime
        """
        pass
