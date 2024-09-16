document.getElementById('create-note-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const title = e.target.title.value;
    const content = e.target.content.value;

    const response = await fetch('/api/notes/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title, content }),
    });

    if (response.ok) {
        window.location.reload();
    } else {
        alert('Failed to create note');
    }
});
