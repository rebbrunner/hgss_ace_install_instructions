# HGSS Wondercard Install

The wondercard installation process has been broken up into many individual codes in order to try and break it down into more manageable, testable chunks.  At first glance the sheer length of the codes may seem overwhelming, but I will emphasize **the first 6 rows do not change the entire time**.  This code is meant to install into slot 2 of a DP save file in order to be compatible with the platinum setup card as well.  The install process is broken down into the following:

1. Creating the copy loop
2. Activating the wondercard
3. Making the card shareable
4. Installing the writer application (2 codes)
5. Escaping the ASE sandbox into full ACE
6. Creating the malformed gift that hijacks an NPC and triggers ASE

## Copy Loop

The copy loop copies data from our dots artist app to our actual wondercard location.

    IMAGE REF

This code will not change throughout the rest of the codes.  It is worth noting that this code in order to save extra space copies over a couple extra unwanted bytes of meta data (packet size, write location offset).  Because of this we install certain sections of the card *backwards*.

## Activating the wonder card

Enter the following 3 codes in order:

    IMAGE REF

    IMAGE REF

    IMAGE REF

Save, restart your game and confirm you should still see your original Pt wondercard (if installed) along side a *new* wondercard.  It will not be shareable at this time.  The three codes are to add the new wondercard, then walkback over the wondercard slots to preserve existing cards showing.  If this code works it also implies your copy loop was successfully written before we move on to the writer app section (the long codes).

## Making the card shareable

Enter the following to make the card shareable:

    IMAGE REF

This code makes it infinitely distributable:

    IMAGE REF

Save, restart your game.  You should now be able to see the option to share your card.  If you want to be extra thorough you can attempt to share to a couple other gen 4 games just to make sure the game version doesn't matter.

## The writer app

We now move on to the actual payload itself which will be deployed onto HGSS.  The codes here can't be quickly verified on DP they were correctly intalled, so go slow and double check.  Since we are splitting the install into a couple sections it's at least possible to get an idea of which section might be off, but you will have to re-send the card if you've made a mistake.

To start things off we're going to add the actual writer application that is responsible for converting box names into executable code defaulted to the player card signature data.

    IMAGE REF

    IMAGE REF

## ASE -> ACE

Our card will not enter fully into ACE initially limiting what we can do.  We start in gen 4's script execution engine instead, which while extremely useful and powerful we want full control.  This next snippet does a couple different things:

- It writes a couple bytes to an unused script function, jumping us out of ASE into full ACE
- It brings up the box so we can easily adjust our boxnames without having to leave the mart
- It makes you ride your bike (technical explanation- shifts instruction alignment parity, for *casual users just consider it validation your code executed*)
- Kicks off the hacked script to drop us into full ACE

    IMAGE REF


## The Gift

The final code installs the actual gift that hijacks the local map NPCs.  I won't spend time explaining this as the opener for this write-up does.

    IMAGE REF

## Setting up HGSS

Once you have your bootstrap pokemon generated (see [Bootstrap]() if not created yet) and your wondercard crafted you are ready to test things on HGSS.  For this section, we use the word `session` to describe executing codes *without leaving the mart*.  Exiting the mart ends the "session".  To setup HGSS do the following:

1. Trade your bootstrap mon to the target HGSS file.
2. Share your wonder card to the target HGSS file.

Now from HGSS:
1. Place the bootstrap mon in slot 5 of your party
2. Fish for an encounter, note you do **not** need to actually enter battle, just getting the hooked message is enough.
3. Without opening any menus or talking to any NPCs, move to the map's local mart and talk to the postman which will hijack an NPC on that map.
4. Talk to the hijacked NPC to execute your first code

*Important Note*:
- The NPC remains hijacked until you leave the mart.
  - We leverage this for [chaining multiple codes in one session](#executing-additional-codes-per-session).

### Executing Additional Codes per Session

After executing one code after first entering the mart, the first run of our writer app sets up an additional feature to make subsequent runs easier as long as you haven't ended the current session.  This means you won't have to do a fish encounter between each code.  This is done by directly editing the NPC's script to point to the first party mon's nickname, instead of bouncing off the in battle PID of party mon 5.

To execute more codes, swap your bootstrap mon from slot 5 into slot 1, then close/reopen your party menu so the moved pokemon updates its location correctly in memory.  You can now continuously talk to the postman to execute codes.

*Important Note*:
Any time you reload graphics it wipes the nickname data out from memory that will result in a crash.  Make sure to re-open your party menu if you do anything such as:
- Open bag
- Open trainer card
- Open options
- Open pokédex
- etc...

If you want to be extra safe, you can open the menu between codes to ensure the nickname is always loaded.

## Debugging

While the first few codes provide quick means to validate they were correct, the last few codes do not.  This section covers what you need to do to rework your card in case of typos.

### Incorrect Gift

**indicators**:
- Postman gives wrong gift
- NPC doesn't execute codes

To fix re-run the following codes in order:
1. [The Gift](#the-gift)

### Incorrect ASE -> ACE Setup

**indicators**:
- Code freezes after talking to hijacked NPC and you either don't get the PC box pop-up or you don't get on your bike

To fix re-run the following codes in order:
1. [ASE -> ACE](#ase---ace)
2. [The Gift](#the-gift)

### Bad Writer App

**indicators**:
- Code freezes after PC box pop-up

*IMPORTANT NOTE* --- If you are trigger a code and it freezes there is a full possibility you made a typo.  Please refer to the checksum images in our [Payloads]() section to validate your code is correct.

To fix re-run the following codes in order (Run *both* of the Writer codes):
1. [Writer Install](#the-writer-app)
2. [ASE -> ACE](#ase---ace)
3. [The Gift](#the-gift)
