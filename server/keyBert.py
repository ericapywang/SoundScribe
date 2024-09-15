
# Import the KeyBERT model
from keybert import KeyBERT

# Initialize the KeyBERT model
kw_model = KeyBERT()

# Define a sample conversation/document
docs = [
    """"As the sun cast a golden hue over the city streets, two jazz musicians bumped into each other outside a familiar café.

"Hey, didn't expect to see you here!" one exclaimed, a smile spreading across his face. "How's it going?"

"Pretty good!" his friend replied, adjusting the strap of his saxophone case. "Just got back from a week in New York."

"No way! What were you doing up there?" the first musician asked, his eyes widening with interest.

"I had a few gigs lined up in some jazz clubs downtown," he said enthusiastically. "Played at the Village Vanguard and even got a last-minute spot at Birdland."

"That's amazing! Those are legendary venues," the first remarked, clearly impressed.

"Tell me about it," his friend agreed. "The energy in New York is something else. The crowd, the atmosphere—it really pushes you to bring your A-game."

"I've always wanted to play in New York," the first musician mused. "Did you get a chance to explore the city?"

"Yeah, between rehearsals and shows, I wandered around Greenwich Village and checked out some jam sessions in Harlem," he replied. "The whole place is steeped in jazz history."

"Sounds like you soaked it all in. Any memorable moments?" his friend asked.

"Actually, yes," he said, his eyes lighting up. "One night after our set, Wynton Marsalis dropped by the club. Ended up jamming with us for a couple of songs."

"You're kidding! That's a once-in-a-lifetime experience," the first musician exclaimed.

"Absolutely. It was surreal," he nodded. "He gave me some pointers afterward—can't put a price on that kind of mentorship."

"Now you've got me itching to book a trip," his friend said eagerly. "Maybe we should plan a gig together up there."

"I'd be up for that," he agreed. "New York has a way of igniting creativity. Plus, it'd be great to share the experience with someone from back home."

"Let's make it happen," the first musician said, his excitement palpable. "In the meantime, you'll have to fill me in on all the details over coffee."

"It's a deal," he laughed. "I've got plenty of stories to tell."

Together, they walked into the café, the aroma of freshly brewed coffee mingling with the distant notes of a jazz melody playing softly in the background. As they found a table by the window, the conversation flowed effortlessly—two kindred spirits sharing their passion for music and the unforgettable allure of New York City.""",
    """**The Vibrant Energy of Boston's Annual Tech Hackathon**

Boston, a city renowned for its rich history and academic prowess, transforms every spring into a buzzing hub of innovation during its annual tech hackathon. The event, hosted in the sprawling halls of the Boston Convention and Exhibition Center, draws thousands of tech enthusiasts, students, and professionals from around the globe.

As the sun rises over the Charles River, participants gather with laptops in hand and ideas brimming in their minds. The hackathon spans 48 intense hours, during which teams collaborate to develop solutions addressing some of the world's most pressing challenges—ranging from healthcare and education to environmental sustainability.

**Day 1: The Kickoff**

The atmosphere on the first day is electric. Attendees are greeted by the sight of towering booths from tech giants like Microsoft, Google, and local startups eager to scout fresh talent. The opening ceremony features keynote speeches from industry leaders and influential innovators. This year, Dr. Emily Chen, a pioneer in artificial intelligence from MIT, captivated the audience with insights into the future of machine learning and its potential societal impacts.

After the formalities, participants dive into networking sessions, forming teams that balance diverse skills—from coding and design to business strategy. Workshops are held throughout the day, offering guidance on the latest technologies, APIs, and development tools available for use during the hackathon.

**Day 2: The Grind**

The second day is a whirlwind of activity. Teams are now deep into the development phase, huddled around tables strewn with notebooks, energy drinks, and half-eaten snacks. The venue hums with the clatter of keyboards and the murmur of collaborative brainstorming.

Mentors roam the floor, offering advice and troubleshooting assistance. Emma Rodriguez, a software engineer from a leading biotech firm, helps a team optimize their app designed to monitor patient vitals remotely. In another corner, a group working on an educational game receives pointers on user experience design from a seasoned UI/UX specialist.

Despite the intense focus, there's a palpable sense of camaraderie. Spontaneous games of ping-pong erupt in the recreation area, and laughter echoes as participants share anecdotes and tips. Food trucks lined up outside offer a respite, serving everything from classic New England clam chowder to international cuisines, fueling both body and spirit.

**Day 3: The Finale**

The final day arrives swiftly, and with it, the deadline. Teams scramble to put the finishing touches on their projects, debugging code and rehearsing presentations. By noon, submissions are closed, and the demonstration booths are set up.

Judges circulate the exhibition hall, evaluating each project on criteria such as innovation, feasibility, and social impact. Projects range from an AI-powered recycling sorter to a blockchain-based platform for transparent charitable donations.

One standout project is "HarborHealth," an app developed by a team of university students aiming to provide real-time water quality monitoring for coastal communities. Using low-cost sensors and data analytics, the app alerts users to pollution levels, promoting public health and environmental stewardship.

**The Awards Ceremony**

As evening falls, participants gather for the awards ceremony. Anticipation hangs in the air as the judges take the stage to announce the winners. "HarborHealth" secures the grand prize, earning accolades for its ingenuity and potential to make a tangible difference.

The People's Choice Award goes to "EduAR," an augmented reality platform that transforms textbook learning into interactive experiences, captivating both educators and tech enthusiasts alike.

**Reflections and Farewells**

The hackathon concludes with a closing party on a rooftop overlooking the city skyline. Under the glow of string lights, participants reflect on their experiences. Friendships have been forged, skills sharpened, and passions ignited. For many, the event is more than a competition—it's a catalyst for future collaborations and a testament to the power of collective creativity.

As attendees disperse, returning to their respective corners of the world, they carry with them not just prizes or new lines on their resumes, but the inspiration to drive change within their communities. The Boston hackathon, with its fusion of historic charm and cutting-edge innovation, leaves an indelible mark on all who partake.

**Looking Ahead**

Plans are already underway for next year's event, promising to be even more expansive and inclusive. Organizers aim to introduce new tracks focusing on artificial intelligence ethics, green technology, and cybersecurity. With Boston's unwavering commitment to fostering innovation, the hackathon is poised to remain a beacon for aspiring technologists and entrepreneurs for years to come.""",
    """Shopping at H Mart is a vibrant and sensory experience. The moment you walk in, you're greeted by aisles filled with exotic fruits, fresh vegetables, and a vast array of Asian groceries. Shelves are stocked with items ranging from Korean kimchi and Japanese snacks to unique sauces and spices. The seafood section boasts live fish and shellfish, ensuring freshness for your culinary adventures. Friendly staff are available to help you navigate unfamiliar ingredients or offer cooking tips. Many shoppers conclude their visit by stopping at the in-store food court, savoring authentic dishes that make the trip both a shopping and cultural delight.
    """,
    """**Band Members:**

- *Chris* (Lead singer)
- *Jess* (Guitarist)
- *Sam* (Drummer)
- *Max* (Bassist)

---

**Chris**: Alright, guys, New York’s just around the corner. How’s everyone feeling about the trip?

**Jess**: I’m pumped! I can’t wait to check out the music scene there. Plus, I’ve got a few guitar shops I wanna hit. Maybe I’ll find that vintage Fender I’ve been dreaming about.

**Max**: Dude, you’ve said that about every city we’ve been to. But yeah, New York’s gonna be insane. I’ve been dying to play there for ages. Madison Square Garden, here we come!

**Sam**: Easy, Max. We’re not quite at the Garden level yet. But yeah, I’ve got my eye on some drum clinics while we’re there. I wanna pick up a few new tricks before we hit the studio again.

**Chris**: Good call. I’ve been thinking about that too. We should squeeze in some studio time while we’re there. You know, get a feel for that New York vibe in the new tracks.

**Jess**: Ooh, that would be cool. Something gritty, raw. Maybe hit up some smaller venues, see what the local bands are doing, and draw some inspiration from the underground scene.

**Max**: For sure! I’m also thinking food. We’ve gotta hit up some classic New York pizza spots. I’m making it my mission to try a slice from every place we pass.

**Sam**: Priorities, right? But seriously, let’s set aside some time for sightseeing too. I’ve never been to the Statue of Liberty, and I wanna do the whole tourist thing.

**Chris**: I’m down. I wanna walk through Central Park too. Maybe we can all hang there after one of the gigs, just chill and soak it in.

**Jess**: Yeah, Central Park sounds cool. But don’t forget, we’ve got to hit up Brooklyn. There’s this rooftop bar with a killer view of the skyline I’ve been dying to check out.

**Max**: Rooftops, live music, pizza, and gear shopping. This trip’s gonna be legendary.

**Sam**: Plus, it’s New York. Who knows what’s gonna happen? We might meet some other artists, get spontaneous jam sessions going. The city’s got that kind of energy.

**Chris**: Totally. Let’s make the most of it. We’ve got gigs lined up, but I want this trip to be more than just work. Let’s explore, soak in the vibe, and maybe even come back with a whole new sound.

**Jess**: New sound? You mean something besides Max’s basslines? *laughs*

**Max**: Hey, my basslines hold this band together! But yeah, let’s come back with something fresh. New York’s gonna change us. I can feel it.

**Sam**: Alright, it’s settled. We play, we explore, and we let New York do its magic. Let’s make this trip one to remember.

**Chris**: Hell yeah. New York, here we come!""",
    "I love green eggs, ham, sausages, and bacon!",
    "The brown fox is quick and the blue dog is lazy!",
    "The sky is very blue and the sky is very beautiful today.",
    "The dog is lazy but the brown fox is quick."]

# Extract keywords using Maximal Marginal Relevance (MMR)
for idx, doc in enumerate(docs):
    print(f"Document {idx}: {doc}")
    
    # Use MMR to get diverse topics, with a diversity factor of 0.7 (more diversity)
    keywords = kw_model.extract_keywords(
        doc, 
        keyphrase_ngram_range=(1, 3), 
        stop_words='english', 
        use_mmr=True,       # Use Maximal Marginal Relevance
        diversity=0.7,      # Increase diversity, range is [0-1]
        top_n=3             # Get 3 diverse topics
    )
    
    print("Extracted Diverse Topics:", keywords)
    print("-" * 50)
