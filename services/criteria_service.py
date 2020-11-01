from datetime import datetime, timedelta

class CriteriaService:

    def build_pattern_prefix(self):
        prefix = []
        dt = datetime.today()
        start = dt - timedelta(days=dt.weekday()+1)
        current = dt - timedelta(days=dt.weekday()+1)
        end = start + timedelta(days=8)

        while current < end:
            prefixo = current.strftime('%m.%d.%y')
            prefix.append(prefixo)
            current = current + timedelta(days=1)        
        
        return prefix