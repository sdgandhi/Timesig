import threading
import curses


def printBar8(curBeat):
	if curBeat == 0:
		return "| | | | | | | | |"
	if curBeat%8 == 0:
		return '| | | | | | | |X|'
	returnStr = []
	returnStr.append('|')
	for i in range(0,curBeat%8-1):
		returnStr.append(' |')
	else:
		returnStr.append('X|')
	for i in range(0,8 - (curBeat%8)):
		if curBeat%8 == 0:
			break
		returnStr.append(' |')

	return ''.join(returnStr)


def printBar16(curBeat):
	if curBeat == 0:
		return "| | | | | | | | | | | | | | | | |"
	if curBeat%16 == 0:
		return '| | | | | | | | | | | | | | | |X|'
	returnStr = []
	returnStr.append('|')
	for i in range(0,curBeat%16-1):
		returnStr.append(' |')
	else:
		returnStr.append('X|')
	for i in range(0,16 - (curBeat%16)):
		if curBeat%16 == 0:
			break
		returnStr.append(' |')

	return ''.join(returnStr)


curBeat = 0
firstPrintLine = 4
tabPrintLine = 5

stdscr = curses.initscr()
curses.resizeterm(25, 120)
curses.noecho()
curses.cbreak()
stdscr.keypad(1)
stdscr.addstr("Welcome to Timesig.\nThis utility keeps track of odd time signatures so you can learn to improvise outside of 4/4.")

stdscr.addstr(firstPrintLine,tabPrintLine,"BEAT NUMBER: ")
stdscr.addstr(firstPrintLine+1,tabPrintLine,"BEATS LEFT IN EIGHT: ")
stdscr.addstr(firstPrintLine+2,tabPrintLine,"BEATS LEFT IN SIXTEEN: ")

while 1:
	ch = stdscr.getch()

	if ch == ord('a'):
		curBeat += 1
		#stdscr.addstr(str(ch))
	if ch == ord('s'):
		curBeat += 1
		#stdscr.addstr(str(ch))
	if ch == ord('d'):
		curBeat += 1
		#stdscr.addstr(str(ch))
	if ch == ord('f'):
		curBeat += 1
		#stdscr.addstr(str(ch))
	if ch == ord('j'):
		curBeat += 1
		#stdscr.addstr(str(ch))
	if ch == ord('k'):
		curBeat += 1
		#stdscr.addstr(str(ch))
	if ch == ord('l'):
		curBeat += 1
		#stdscr.addstr(str(ch))
	if ch == ord(';'):
		curBeat += 1
		#stdscr.addstr(str(ch))
	if ch == ord('r'):
		curBeat = 0

	if curBeat%8 ==1:
		curses.flash()
	
	stdscr.addstr(firstPrintLine,tabPrintLine,"BEAT NUMBER: " + str(curBeat) + "     ")
	#stdscr.addstr(firstPrintLine+1,50,"BEATS LEFT IN EIGHT: " + str(8-(curBeat%8)) + "     ")
	stdscr.addstr(firstPrintLine+1,tabPrintLine,"BEATS LEFT IN EIGHT:   " + printBar8(curBeat))
	#stdscr.addstr(firstPrintLine+2,10,"BEATS LEFT IN SIXTEEN: " + str(16-(curBeat%16)) + "     ")
	stdscr.addstr(firstPrintLine+2,tabPrintLine,"BEATS LEFT IN SIXTEEN: " + printBar16(curBeat))

	stdscr.move(0,0)

curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()

