from bitgenesis.memory.memory_attention import MemoryAttention
from bitgenesis.memory.memory_context import MemoryContext

from bitgenesis.reasoning.context import ReasoningContext
from bitgenesis.reasoning.engine import ReasoningEngine


class ReasoningSession:

    def __init__(self, memory_store):

        self.memory_store = memory_store
        self.engine = ReasoningEngine()

    def process(self, event):

        # Recupera tutte le memorie
        memories = self.memory_store.all()

        # Seleziona quelle più rilevanti
        attended = MemoryAttention.select(memories)

        # Costruisce il contesto della memoria
        memory_context = MemoryContext.build(attended)

        # Costruisce il contesto di ragionamento
        context = ReasoningContext(
            event=event,
            memory_store=self.memory_store,
            memory_context=memory_context,
        )

        # Avvia il motore decisionale
        return self.engine.evaluate(context)