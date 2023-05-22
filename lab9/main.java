
import java.io.*;

class lab9 {
	public static void main(String[] args) throws IOException {
		//System.out.println("Hello, World!");
		BufferedReader bufferReader = new BufferedReader(new InputStreamReader(System.in));
		//Scanner sc=new Scanner(System.in);

		String format_string, param;
		if (!bufferReader.ready()) {
			my_printf(
					"TEST9 #.1h",
					"2315"
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
				if ((format_string.charAt(i) == '#') && (format_string.charAt(i + 1) == 'h')) {
					outstr.append(modifyOutNumber(String.format("%f", Float.parseFloat(param))));
					i++;
					toAppend = false;
				}
				//////////////////////////////////////////
				if (toAppend && (format_string.charAt(i) == '#')
						&& format_string.charAt(i + 1) == '.' && Character.isDigit(format_string.charAt(i + 2))
				) {
					String paramReformatted;
					int charToSkip = 0;
					Integer maxParamLen = null;

					if (format_string.charAt(i + charToSkip + 1) == '.') {
						charToSkip++;
						int numLen = 1;
						while (Character.isDigit(format_string.charAt(i + charToSkip + numLen))) {
							numLen++;
						}
						numLen--;
						maxParamLen = Integer.parseInt(format_string.substring(i + charToSkip + 1, i + charToSkip + numLen + 1));
						charToSkip += numLen;
					}

					if (format_string.charAt(i + charToSkip + 1) == 'h') {
						charToSkip++;
						paramReformatted = String.format("%" + "." + maxParamLen + "f", Float.parseFloat(param));
						outstr.append(modifyOutNumber(paramReformatted));
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

	public static String modifyOutNumber(String number) {
		return number
				.replaceAll(",", ".");

	}
}
