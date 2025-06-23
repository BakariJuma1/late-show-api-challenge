
from server.app import db, create_app
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.models.user import User

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    print("🌱 Seeding database...")

    # Clear existing data
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()
    User.query.delete()

    # Create test user
    user = User(username="bakari")
    user.set_password("123456")

    # Create guests
    guest1 = Guest(name="Lupita Nyong'o", occupation="Actor")
    guest2 = Guest(name="Eliud Kipchoge", occupation="Athlete")

    # Create episodes
    episode1 = Episode(date="2024-05-01", number=1)
    episode2 = Episode(date="2024-05-02", number=2)

    # Create appearances
    appearance1 = Appearance(rating=5, guest=guest1, episode=episode1)
    appearance2 = Appearance(rating=4, guest=guest2, episode=episode1)
    appearance3 = Appearance(rating=3, guest=guest2, episode=episode2)

    # Add to session
    db.session.add_all([user, guest1, guest2, episode1, episode2, appearance1, appearance2, appearance3])
    db.session.commit()

    print("✅ Done seeding!")
