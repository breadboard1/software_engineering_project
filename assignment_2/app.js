const loadData = async () => {
  try {
    const res = await fetch(
      `https://openapi.programming-hero.com/api/videos/categories`
    );
    const data = await res.json();
    displayMenu(data.data);
    displayBody();
  } catch (err) {
    console.error(err);
  }
};

const displayMenu = (data) => {
  const menuContainer = document.getElementById("menu-container");
  data.forEach((element) => {
    console.log(element.category);
    const card = document.createElement("p");
    card.classList.add("card-box");
    card.innerHTML = `
    <button
        onclick = "displayBody(${element.category_id})"
        type="button"
      >
      ${element.category}
      </button>
    `;
    menuContainer.appendChild(card);
  });
};

const displayBody = async (id = 1000) => {
  try {
    const response = await fetch(
      `https://openapi.programming-hero.com/api/videos/category/${id}`
    );
    const data = await response.json();
    const videoContainer = document.getElementById("video-container");
    console.log(data);
    videoContainer.innerHTML = "";
    if (data.data.length == 0) {
      const card = document.createElement("div");
      card.innerHTML = `
      <div class="no-icon-warning">
        <img id="nothing-box" src="./PHero-Tube-main/Icon.png" alt="">
        <br>
        <h1>Oops!! Sorry, There is no content here</h1>
      </div>
      `;
      videoContainer.appendChild(card);
      return;
    }
    data.data.forEach((element) => {
      const card = document.createElement("div");
      card.classList.add("video-box");
      card.innerHTML = `
      <img class="thumbnail-box" src="${element.thumbnail}" alt="">
      <br>
      <div class = "profile-title-container">
        <img class="profile-box" src="${
          element.authors[0].profile_picture
        }" alt="">
        <h3>${element.title}</h3>
      </div>
      <div class = "name-verification-container">
        <p>${element.authors[0].profile_name}</p>
        <img class="verified-box" src="${
          element.authors[0].verified ? "./PHero-Tube-main/verified.png" : ""
        }" alt="">
      </div>
      <p>${element.others.views} views</p>
      `;
      videoContainer.appendChild(card);
    });
  } catch {
    (err) => {
      console.log(err);
    };
  }
};

const displaySorted = async () => {
  try {
    const response = await fetch(
      `https://openapi.programming-hero.com/api/videos/category/1000`
    );
    const data = await response.json();
    const videoContainer = document.getElementById("video-container");
    console.log(data);
    videoContainer.innerHTML = "";
    data.data.sort(
      (a, b) =>
        stringToInteger(b.others.views) - stringToInteger(a.others.views)
    );
    data.data.forEach((element) => {
      const card = document.createElement("div");
      card.classList.add("video-box");
      card.innerHTML = `
      <img class="thumbnail-box" src="${element.thumbnail}" alt="">
      <br>
      <div class = "profile-title-container">
        <img class="profile-box" src="${
          element.authors[0].profile_picture
        }" alt="">
        <h3>${element.title}</h3>
      </div>
      <div class = "name-verification-container">
        <p>${element.authors[0].profile_name}</p>
        <img class="verified-box" src="${
          element.authors[0].verified ? "./PHero-Tube-main/verified.png" : ""
        }" alt="">
      </div>
      <p>${element.others.views} views</p>
      `;
      videoContainer.appendChild(card);
    });
  } catch {
    (err) => {
      console.log(err);
    };
  }
};

const stringToInteger = (num) => {
  const value = parseFloat(num);
  if (num[num.length - 1] == "K") {
    return value * 1000;
  } else if (num[num.length - 1] == "M") {
    return value * 1000000;
  }
};

loadData();
