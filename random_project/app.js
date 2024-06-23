const loadData = (global) => {
  const data = fetch("https://jsonplaceholder.typicode.com/posts/1/comments")
    .then((res) => res.json())
    .then((data) => displayData(data));
};

const displayData = (data) => {
  const commentContainer = document.getElementById("comment-container");
  console.log(data);
  data.forEach((comment) => {
    const card = document.createElement("div");
    card.classList.add("comment-box");
    card.innerHTML = `
        <h3>${comment.name}</h3>
        <h4>${comment.email}</h4>
        <p>${comment.body}</p>
    `;
    commentContainer.appendChild(card);
  });
};

loadData("comments");
