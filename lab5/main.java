
import java.io.*;

class lab5 {
	public static void main(String[] args) throws IOException {
		//System.out.println("Hello, World!");
		BufferedReader bufferReader = new BufferedReader(new InputStreamReader(System.in));
		//Scanner sc=new Scanner(System.in);

		String format_string, param;
		if (!bufferReader.ready()) {
			my_printf(
					"test#8ghh123",
					"1204"
			);

		}
		while (bufferReader.ready()) {
			format_string = bufferReader.readLine();
			param = bufferReader.readLine();
			my_printf(format_string, param);
		}

	}

    public static void my_printf(String format_string, String param) {
        StringBuilder outstr = new StringBuilder();
		boolean toAppend;
        for (int i = 0; i < format_string.length(); i++) {
			toAppend = true;

			try {
				if ((format_string.charAt(i) == '#') && (format_string.charAt(i + 1) == 'g')) {
					outstr.append(everyDigitMinusOne(param));
					i++;
					toAppend = false;
				}
				//////////////////////////////////////////
				if (toAppend && (format_string.charAt(i) == '#') && (Character.isDigit(format_string.charAt(i + 1)))) {
					String paramReformatted;
					int charToSkip = 0;
					Integer minParamLen = null;

					if (Character.isDigit(format_string.charAt(i + charToSkip + 1))) {
						int numLen = 1;
						while (Character.isDigit(format_string.charAt(i + charToSkip + numLen))) {
							numLen++;
						}
						numLen--;
						minParamLen = Integer.parseInt(format_string.substring(i + charToSkip + 1, i + charToSkip + numLen + 1));
						charToSkip += numLen;
					}

					if (format_string.charAt(i + charToSkip + 1) == 'g') {
						charToSkip++;
						paramReformatted = String.format("%" + minParamLen + "s", param);
						outstr.append(everyDigitMinusOne(paramReformatted));
						i += charToSkip;
						toAppend = false;
					}
				}
			} catch (Exception ignored) {

			} finally {
				if(toAppend) {
					outstr.append(format_string.charAt(i));
				}
			}

        }
        System.out.println(outstr.toString());
    }

	public static String everyDigitMinusOne(String number) {
		StringBuilder outStr = new StringBuilder();
		for (char c : number.toCharArray()) {
			if(Character.isDigit(c)) {
				if (c == '0') {
					c = '9';
				} else {
					c = (char) (c - 1);
				}
			}
			outStr.append(c);
		}
		return outStr.toString();
	}
}
